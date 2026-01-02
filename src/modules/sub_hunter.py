# src/modules/sub_hunter.py (INTERNET SCANNER VERSION)
import requests
import json
from src.core.utils import print_emaz

def discover_subdomains(master_domain):
    """
    Internet ke certificates (crt.sh) se saare real-time subdomains dhoondta hai.
    """
    print_emaz(f"Searching Internet Databases for: {master_domain}...", "INFO")
    
    # crt.sh API URL
    url = f"https://crt.sh/?q=%25.{master_domain}&output=json"
    
    try:
        response = requests.get(url, timeout=20)
        if response.status_code != 200:
            print_emaz("Internet database busy. Using local patterns...", "ERROR")
            return ['dev', 'test', 'stage', 'api'] # Fallback
        
        data = response.json()
        # Sirf unique domain names nikaalna
        discovered = set()
        for entry in data:
            name = entry['name_value'].lower()
            # Wildcards (*) saaf karna
            if "*" not in name:
                discovered.add(name)
        
        print_emaz(f"FOUND {len(discovered)} REAL DOMAINS ON INTERNET!", "SUCCESS")
        return list(discovered)
        
    except Exception as e:
        print_emaz(f"Scanner Error: {str(e)}", "ERROR")
        return []