# src/modules/validator.py
import requests
from src.core.utils import print_emaz

def validate_takeover(url, keyword="Hello world"):
    print_emaz(f"Validating: {url}...", "INFO")
    
    try:
        # User-Agent lagana zaroori hai taake request block na ho
        headers = {'User-Agent': 'Mozilla/5.0 (EMAZ-Tester)'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200 and keyword in response.text:
            print_emaz(f"VALIDATION SUCCESS! Found '{keyword}'", "SUCCESS")
            return True
        else:
            # Ab ye ERROR ki tafseel (Detail) batayega
            print_emaz(f"Validation Failed. Status: {response.status_code}", "ERROR")
            
            # Agar chota error hai to print karo
            if len(response.text) < 200:
                print_emaz(f"Server Response: {response.text}", "ERROR")
            else:
                print_emaz(f"Server Response (First 100 chars): {response.text[:100]}...", "ERROR")
            
            return False
            
    except requests.exceptions.RequestException as e:
        print_emaz(f"Connection Error: {e}", "ERROR")
        return False