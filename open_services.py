"""
Simply open all consignment services
Each service handles its own authentication
"""

from browser import Browser
import time

services = [
    ("Admin", "http://localhost:5003"),
    ("Catalog", "http://localhost:5004"),
    ("Login", "http://localhost:5002"),
    ("API Docs", "http://localhost:5001/docs")
]

browser = Browser(headless=False)

try:
    # Open first service
    print(f"Opening {services[0][0]} at {services[0][1]}...")
    browser.goto(services[0][1])
    time.sleep(1)
    
    # Open rest in new tabs
    for name, url in services[1:]:
        print(f"Opening {name} at {url} in new tab...")
        browser.driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(0.3)
    
    print("\n✓ All services opened!")
    print("\nTabs:")
    for name, url in services:
        print(f"  - {name}: {url}")
    
    print("\nLogin to each service as needed.")
    print("Press Ctrl+C to close all tabs...")
    
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nClosing browser...")
    browser.close()
