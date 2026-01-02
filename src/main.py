# src/main.py (ACCURATE HUNTER)
import sys, os, time, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.utils import print_emaz, banner
from src.modules.sub_hunter import discover_subdomains
from src.modules.dns_analyzer import analyze_dns
from src.modules.fastly_api import create_service

def main():
    banner()
    print_emaz("CHALLENGE: 97.1% ACCURACY ENGAGED", "INFO")
    
    user_input = input("\nEnter Master Domain: ")
    # Multi-domain support with clean split
    master_list = [d.strip() for d in user_input.replace(',', ' ').split() if d.strip()]
    
    for master in master_list:
        targets = discover_subdomains(master)
        for target in targets:
            # Silence the trash, only show what matters
            if analyze_dns(target):
                print_emaz(f"FOUND ACCURATE TARGET: {target}", "SUCCESS")
                # Immediate Takeover
                link = create_service(target)
                if link:
                    # JSON Logging
                    log_file = os.path.join("data", "success_logs.json")
                    log_entry = {"domain": target, "poc": link, "time": time.ctime()}
                    data = []
                    if os.path.exists(log_file):
                        with open(log_file, 'r') as f:
                            try: data = json.load(f)
                            except: data = []
                    data.append(log_entry)
                    with open(log_file, 'w') as f:
                        json.dump(data, f, indent=4)
                    print_emaz(f"SAVED: {target}", "SUCCESS")
            else:
                # Sirf scan progress dikhaye taake aapko lage ke kaam ho raha hai
                sys.stdout.write(f"\r[EMAZ INFO] Scanning: {target[:40]}...  ")
                sys.stdout.flush()

if __name__ == "__main__":
    main()