"""
Inspect the login page to understand its structure
"""

from browser import Browser
import time

browser = Browser(headless=False)

try:
    print("Opening login page...")
    browser.goto("http://localhost:5002")
    time.sleep(2)

    # Get page source
    page_source = browser.driver.page_source

    # Save to file
    with open("login_page.html", "w") as f:
        f.write(page_source)

    print("Page source saved to login_page.html")
    print("\nPage title:", browser.driver.title)
    print("Current URL:", browser.driver.current_url)

    # Try to find form elements
    print("\nLooking for form elements...")

    try:
        forms = browser.find_all("form")
        print(f"Found {len(forms)} form(s)")

        inputs = browser.find_all("input")
        print(f"Found {len(inputs)} input(s)")
        for inp in inputs:
            print(
                f"  - type: {inp.get_attribute('type')}, name: {inp.get_attribute('name')}, id: {inp.get_attribute('id')}"
            )

        buttons = browser.find_all("button")
        print(f"Found {len(buttons)} button(s)")
        for btn in buttons:
            print(f"  - type: {btn.get_attribute('type')}, text: {btn.text}")

    except Exception as e:
        print(f"Error finding elements: {e}")

    print("\nKeeping browser open for inspection. Press Ctrl+C to close...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nClosing browser...")
    browser.close()
