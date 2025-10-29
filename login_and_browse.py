"""
Login to consignment system and open all services
"""

from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = Browser(headless=False)

try:
    print("Step 1: Opening login page...")
    browser.goto("http://localhost:5002")
    time.sleep(1)
    
    print("Step 2: Filling credentials...")
    username_field = browser.find("#username")
    password_field = browser.find("#password")
    
    username_field.send_keys("admin")
    password_field.send_keys("admin123")
    
    print("Step 3: Submitting login...")
    submit_btn = browser.find("button[type='submit']")
    submit_btn.click()
    
    print("Step 4: Waiting for redirect to admin...")
    # Wait for URL to change (redirect happens)
    time.sleep(3)
    
    current_url = browser.driver.current_url
    print(f"Current URL: {current_url}")
    
    # Save page source for debugging
    with open("after_login.html", "w") as f:
        f.write(browser.driver.page_source)
    
    # If we're on admin page with token, we're good
    if "localhost:5003" in current_url and "token=" in current_url:
        print("✓ Successfully logged in and redirected to admin!")
    else:
        print("Login completed but checking current page...")
    
    # Open other services in tabs
    services = [
        ("Catalog", "http://localhost:5004"),
        ("API Docs", "http://localhost:5001/docs")
    ]
    
    print("\nStep 5: Opening other services...")
    for name, url in services:
        print(f"  Opening {name}...")
        browser.driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(0.5)
    
    print("\n✓ All services opened!")
    print(f"\nTabs open:")
    print(f"  - Admin: {browser.driver.current_url}")
    for name, url in services:
        print(f"  - {name}: {url}")
    
    print("\nPress Ctrl+C to close...")
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nClosing...")
    browser.close()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    print("\nBrowser will stay open. Press Ctrl+C to close...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        browser.close()
