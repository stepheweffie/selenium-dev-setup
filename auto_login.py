"""
Auto-login to consignment services and open all tabs
"""

from browser import Browser
import time
import sys


def auto_login(username, password):
    """
    Open all consignment services and handle login.
    Login on one tab, then manually navigate to others as needed.

    Args:
        username: Login username
        password: Login password
    """

    services = {
        "Login": "http://localhost:5002",
        "Admin": "http://localhost:5003",
        "Catalog": "http://localhost:5004",
        "API Docs": "http://localhost:5001/docs",
    }

    browser = Browser(headless=False)

    try:
        # Go to login page
        print("Opening login page...")
        browser.goto(services["Login"])
        time.sleep(2)

        # Try to auto-fill and submit
        print(f"Attempting to login as {username}...")
        try:
            username_field = browser.wait_for(
                "input[name='username'], input[type='text'], #username", timeout=3
            )
            username_field.clear()
            username_field.send_keys(username)

            password_field = browser.find(
                "input[name='password'], input[type='password'], #password"
            )
            password_field.clear()
            password_field.send_keys(password)

            print("✓ Credentials filled.")

            # Try to find and click submit button
            try:
                submit_btn = browser.find(
                    "button[type='submit'], input[type='submit'], button:contains('Login'), button:contains('Sign in')"
                )
                print("Clicking login button...")
                submit_btn.click()
            except Exception:
                print("Submitting form via Enter key...")
                password_field.submit()

            print("Waiting for login to complete...")
            time.sleep(3)

            current_url = browser.driver.current_url
            print(f"Current URL: {current_url}")

        except Exception as e:
            print(f"Error during login: {e}")
            print("Please complete login manually if needed.")
            input("Press Enter to continue...")

        # Open other services in new tabs
        for name, url in list(services.items())[1:]:
            print(f"Opening {name} at {url} in new tab...")
            browser.driver.execute_script(f"window.open('{url}', '_blank');")
            time.sleep(0.5)

        print("\n✓ All services opened and logged in!")
        print("\nTabs:")
        for name, url in services.items():
            print(f"  - {name}: {url}")

        print("\nPress Ctrl+C to close all tabs...")

        # Keep browser open
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nClosing browser...")
        browser.close()
    except Exception as e:
        print(f"\nError: {e}")
        print("Browser will stay open for manual inspection. Press Ctrl+C to close.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python auto_login.py <username> <password>")
        print("Example: python auto_login.py admin mypassword")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    auto_login(username, password)
