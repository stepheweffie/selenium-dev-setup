"""
Localhost Browser - Automatically visit and interact with localhost apps
"""

from browser import Browser
import time


def visit_localhost(port=3000, path="", headless=False):
    """
    Visit localhost application.

    Args:
        port: Port number (default 3000)
        path: Optional path after domain (e.g., "/dashboard")
        headless: Run in headless mode
    """
    url = f"http://localhost:{port}{path}"

    with Browser(headless=headless) as browser:
        print(f"Opening {url}...")
        browser.goto(url)

        # Keep browser open for interaction
        print("Browser is open. Press Ctrl+C to close.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nClosing browser...")


if __name__ == "__main__":
    import sys

    # Parse command line arguments
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    path = sys.argv[2] if len(sys.argv) > 2 else ""

    visit_localhost(port=port, path=path)
