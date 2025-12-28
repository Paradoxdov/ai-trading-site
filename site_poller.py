import requests
import time
import sys

URL = "https://Paradoxdov.github.io/ai-trading-site/"
MAX_RETRIES = 30  # 5 minutes (30 * 10s)
WAIT_SECONDS = 10

print(f"Polling {URL} for 200 OK...")

for i in range(MAX_RETRIES):
    try:
        response = requests.get(URL)
        print(f"Attempt {i+1}: Status Code {response.status_code}")
        
        if response.status_code == 200:
            # Double check content isn't a 404 page served with 200 (GitHub sometimes does this for custom 404s, though usually 404 status)
            if "There isn't a GitHub Pages site here" not in response.text:
                print("SUCCESS: Site is live!")
                sys.exit(0)
            else:
                print("Got 200, but content looks like default 404 page.")
        
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(WAIT_SECONDS)

print("TIMEOUT: Site did not go live in time.")
sys.exit(1)
