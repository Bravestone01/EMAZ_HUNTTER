# src/core/utils.py
import time
from colorama import Fore, Style, init
import sys
from .config import DELAY_SHORT

init(autoreset=True)

def print_emaz(text, type="INFO"):
    # 27 Padding Logic applied here
    prefix = ""
    if type == "INFO":
        prefix = f"{Fore.CYAN}[EMAZ INFO]{Style.RESET_ALL}"
    elif type == "SUCCESS":
        prefix = f"{Fore.GREEN}[EMAZ WIN ]{Style.RESET_ALL}"
    elif type == "ERROR":
        prefix = f"{Fore.RED}[EMAZ ERR ]{Style.RESET_ALL}"
    
    # 300ms Delay for immersive feel
    time.sleep(DELAY_SHORT)
    print(f"{prefix.ljust(27)} : {text}")

def banner():
    print(f"{Fore.BLUE}{'='*60}")
    print(f"{Fore.CYAN}   EMAZ FASTLY AUTOMATION - 369 LOGIC ENABLED")
    print(f"{Fore.BLUE}{'='*60}{Style.RESET_ALL}\n")