"""
Open consignment services - login manually on the login page
"""

from browser import Browser
import time

browser = Browser(headless=False)

try:
    print("Opening login page...")
    print("Please log in manually with: admin / admin123")
    print("")
    
    browser.goto("http://localhost:5002")
    time.sleep(2)
    
    # Pre-fill credentials to make it easier
    try:
        username_field = browser.wait_for("#username", timeout=5)
        password_field = browser.wait_for("#password", timeout=5)
        
        username_field.clear()
        username_field.send_keys("admin")
        password_field.clear()
        password_field.send_keys("admin123")
        print("✓ Credentials pre-filled. Click 'Sign In' button.")
    except Exception as e:
        print(f"Could not pre-fill credentials: {e}")
        print("Please fill them in manually.")
    
    input("\nPress Enter after you've logged in and landed on the admin page...")
    
    # Open other services in tabs
    services = [
        ("Catalog", "http://localhost:5004"),
        ("API Docs", "http://localhost:5001/docs")
    ]
    
    print("\nOpening other services...")
    for name, url in services:
        print(f"  Opening {name}...")
        browser.driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(0.3)
    
    print("\n✓ All services opened!")
    print("Press Ctrl+C to close...")
    
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nClosing browser...")
    browser.close()
