"""
Visit all consignment services in separate tabs
"""

from browser import Browser
import time


def visit_all_services():
    """Open all consignment services in separate browser tabs."""
    
    services = {
        "API": "http://localhost:5001",
        "Login": "http://localhost:5002",
        "Admin": "http://localhost:5003",
        "Catalog": "http://localhost:5004"
    }
    
    browser = Browser(headless=False)
    
    try:
        # Visit first service
        first_service = list(services.items())[0]
        print(f"Opening {first_service[0]} at {first_service[1]}...")
        browser.goto(first_service[1])
        
        # Open remaining services in new tabs
        for name, url in list(services.items())[1:]:
            print(f"Opening {name} at {url} in new tab...")
            browser.driver.execute_script(f"window.open('{url}', '_blank');")
            time.sleep(0.5)
        
        print("\nAll services opened!")
        print("Tabs:")
        for name, url in services.items():
            print(f"  - {name}: {url}")
        
        print("\nPress Ctrl+C to close all tabs...")
        
        # Keep browser open
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nClosing browser...")
        browser.close()


if __name__ == "__main__":
    visit_all_services()
