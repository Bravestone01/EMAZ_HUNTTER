# src/modules/fastly_api.py (NON-STOP VERSION)
import requests
import time
import random
from src.core.config import API_TOKEN, ORIGIN_HOST
from src.core.utils import print_emaz

BASE_URL = "https://api.fastly.com"

headers = {
    "Fastly-Key": API_TOKEN,
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_service(domain_name):
    # --- UNIQUE NAME LOGIC (Error Khatam) ---
    # Har baar naam ke aage ek random number lagayega taake "Duplicate" na bole
    unique_id = f"{int(time.time())}-{random.randint(100, 999)}"
    service_name = f"EMAZ-{unique_id}"
    # ----------------------------------------
    
    # 1. Create Service
    print_emaz(f"Creating Service: {service_name}...", "INFO")
    resp = requests.post(f"{BASE_URL}/service", headers=headers, data={"name": service_name})
    
    if resp.status_code != 200:
        # Agar error aaye to user ko bataye aur agle domain ke liye 'None' return kare
        print_emaz(f"Failed to create service. Server said: {resp.text}", "ERROR")
        return None
    
    service_id = resp.json()['id']
    version = 1
    
    # 2. Add Domain
    print_emaz(f"Adding Domain: {domain_name}...", "INFO")
    dom_resp = requests.post(f"{BASE_URL}/service/{service_id}/version/{version}/domain", 
                  headers=headers, data={"name": domain_name})
    
    # Agar Domain add nahi hua (maslan pehle se kisi aur account mein hai)
    if dom_resp.status_code != 200:
        print_emaz(f"Skipping {domain_name}: Domain already taken or invalid.", "ERROR")
        return None

    # 3. Add Backend (Github Origin)
    print_emaz(f"Configuring Origin & Override Host...", "INFO")
    backend_data = {
        "hostname": ORIGIN_HOST,
        "address": ORIGIN_HOST,
        "port": 443,
        "use_ssl": 1,          # Fix for SSL
        "ssl_check_cert": 1,
        "ssl_cert_hostname": ORIGIN_HOST,
        "ssl_sni_hostname": ORIGIN_HOST,
        "override_host": ORIGIN_HOST,
        "name": "GitHub-Origin"
    }
    requests.post(f"{BASE_URL}/service/{service_id}/version/{version}/backend", 
                  headers=headers, data=backend_data)

    # 4. Activate
    print_emaz(f"Activating Service...", "INFO")
    act_resp = requests.put(f"{BASE_URL}/service/{service_id}/version/{version}/activate", headers=headers)
    
    if act_resp.status_code == 200:
        print_emaz(f"System ACTIVE for {domain_name}", "SUCCESS")
        return f"http://{domain_name}/ford-poc/syed_mujtaba.html"
    else:
        print_emaz(f"Activation Failed: {act_resp.text}", "ERROR")
        return None