# src/core/config.py

# EMAZ 369 Configuration
API_TOKEN = "w0d1mYDCUJnPS2WaLTP7PVNoA_Vpma41"  # Fastly Profile > API Tokens se len
USER_EMAIL = "apka_email@example.com"

# Origin Details (Jo humne fix kiya tha)
ORIGIN_HOST = "bravestone01.github.io"
ORIGIN_PORT = 443

# 369 Logic Delays (Seconds)
DELAY_SHORT = 0.3   # 300ms (Fast actions)
DELAY_MEDIUM = 0.9  # 900ms (Transitions)
DELAY_LONG = 3.0    # 3s (API Limits / Heavy Loads)

# Retry Logic
MAX_RETRIES = 3