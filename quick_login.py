"""
Quick login - navigate directly to the admin page after login
"""

from browser import Browser
import requests
import time

# First get the token via API
print("Getting auth token...")
response = requests.post(
    "http://localhost:5001/api/auth/login",
    json={"username": "admin", "password": "admin123"},
)

if response.status_code == 200:
    token = response.json()["access_token"]
    print(f"✓ Got token: {token[:50]}...")

    # Now open browser and navigate to admin with token
    browser = Browser(headless=False)

    try:
        print("\nOpening admin with token...")
        browser.goto(f"http://localhost:5003/auth?token={token}")
        time.sleep(2)

        print(f"Current URL: {browser.driver.current_url}")

        # Open other services
        services = [
            ("Catalog", "http://localhost:5004"),
            ("API Docs", "http://localhost:5001/docs"),
        ]

        for name, url in services:
            print(f"Opening {name}...")
            browser.driver.execute_script(f"window.open('{url}', '_blank');")
            time.sleep(0.3)

        print("\n✓ All services opened and logged in!")
        print("\nPress Ctrl+C to close...")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nClosing...")
        browser.close()
else:
    print(f"Login failed: {response.status_code} - {response.text}")
