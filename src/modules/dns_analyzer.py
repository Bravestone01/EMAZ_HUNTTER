# src/modules/dns_analyzer.py (MONEY VERIFIER)
import socket
import requests
from src.core.utils import print_emaz

def analyze_dns(domain):
    """
    Sirf wahi domain pasand karta hai jo 'Fastly Unknown Domain' error de raha ho.
    """
    try:
        # 1. Pehle CNAME check karo
        data = socket.gethostbyname_ex(domain)
        cname_found = False
        for alias in data[1]:
            if 'fastly' in alias.lower():
                cname_found = True
                break
        
        if not cname_found: return False

        # 2. Ab check karo kya ye error de raha hai? (Asli Paisa yahan hai)
        try:
            # Fastly ke error ko pakadne ke liye request bhejte hain
            r = requests.get(f"http://{domain}", timeout=5)
            # Agar 'Fastly error: unknown domain' nazar aaye to ye 100% BOUNTY hai
            if "unknown domain" in r.text.lower() or r.status_code == 404:
                print_emaz(f"CASH DETECTED: {domain} is vulnerable!", "SUCCESS")
                return True
        except:
            # Agar connection fail ho (unreachable), tab bhi takeover ka chance hota hai
            return True
            
        return False
    except:
        return False