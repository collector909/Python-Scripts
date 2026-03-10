# Blind SQL Injection Brute Force Script

A Python script for exploiting blind SQL injection vulnerabilities (PortSwigger Web Security Academy labs).

## Usage

1. Intercept a request in Burp Suite
2. Find the URL, TrackingId and session cookie values
3. Insert them into the script
4. Run: `python3 blind_sqli.py`

## Requirements

pip install requests