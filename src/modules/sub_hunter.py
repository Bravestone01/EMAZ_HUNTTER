# src/modules/sub_hunter.py (ULTIMATE VERSION)
import requests
from src.core.utils import print_emaz

def discover_subdomains(master_domain):
    print_emaz(f"UNLEASHING BEAST: Deep Hunting Ford on Internet...", "INFO")
    discovered = set()

    # Database Search
    try:
        url = f"https://crt.sh/?q=%25.{master_domain}&output=json"
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            for entry in r.json():
                name = entry['name_value'].lower()
                if "*" not in name: discovered.add(name)
    except:
        print_emaz("Internet DB busy, using Internal Intelligence...", "ERROR")

    # Extreme Recursive Patterns (Ford's Hidden Assets)
    extra_patterns = [
        'fastly', 'edge', 'origin', 'cdn', 'static', 'assets',
        'dev-cdn', 'qa-cdn', 'stg-cdn', 'prod-cdn',
        'fastly-test', 'fastly-dev', 'fastly-qa'
    ]
    
    for p in extra_patterns:
        discovered.add(f"{p}.{master_domain}")
        discovered.add(f"{p}.global.{master_domain}")
        # Recursive check for deeper layers
        discovered.add(f"origin.{p}.{master_domain}")

    print_emaz(f"TOTAL SHIKAAR FOUND: {len(discovered)}", "SUCCESS")
    return list(discovered)