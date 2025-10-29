"""
Test the login flow and see what happens after authentication
"""

from browser import Browser
import time

browser = Browser(headless=False)

try:
    print("Opening login page...")
    browser.goto("http://localhost:5002")
    time.sleep(2)

    print("Filling credentials...")
    username_field = browser.find("#username")
    password_field = browser.find("#password")

    username_field.send_keys("admin")
    password_field.send_keys("admin123")

    print("Submitting form...")
    submit_btn = browser.find("button[type='submit']")
    submit_btn.click()

    print("Waiting for redirect...")
    time.sleep(3)

    print(f"\nAfter login:")
    print(f"  URL: {browser.driver.current_url}")
    print(f"  Title: {browser.driver.title}")

    # Check for error messages
    try:
        alerts = browser.find_all(".alert, .error, .alert-danger, .text-danger")
        if alerts:
            print(f"\nError messages found:")
            for alert in alerts:
                if alert.text.strip():
                    print(f"  - {alert.text.strip()}")
    except:
        pass

    # Check page text for any error indicators
    page_text = browser.driver.find_element("tag name", "body").text
    if "invalid" in page_text.lower() or "error" in page_text.lower():
        print(f"\nPage contains error text:")
        print(page_text[:500])

    # Check cookies
    cookies = browser.driver.get_cookies()
    print(f"\nCookies ({len(cookies)}):")
    for cookie in cookies:
        print(f"  - {cookie['name']}: {cookie['value'][:50]}...")

    # Check localStorage
    print("\nLocalStorage:")
    local_storage = browser.driver.execute_script("return Object.keys(localStorage);")
    for key in local_storage:
        value = browser.driver.execute_script(f"return localStorage.getItem('{key}');")
        print(f"  - {key}: {value[:100] if value else 'None'}...")

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
    input("Press Enter to close...")
    browser.close()
