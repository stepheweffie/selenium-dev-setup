"""
Selenium Browser Utility for Development
Provides easy-to-use browser automation with automatic driver management.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:
    """Wrapper class for Selenium WebDriver with dev-friendly defaults."""

    def __init__(self, headless=False, window_size=(1920, 1080)):
        """
        Initialize browser instance.

        Args:
            headless: Run browser in headless mode (no GUI)
            window_size: Tuple of (width, height) for browser window
        """
        self.options = Options()

        if headless:
            self.options.add_argument("--headless=new")

        self.options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Initialize driver with automatic driver management
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=self.options
        )
        self.wait = WebDriverWait(self.driver, 10)

    def goto(self, url):
        """Navigate to URL."""
        self.driver.get(url)
        return self

    def find(self, selector, by=By.CSS_SELECTOR):
        """Find element by selector."""
        return self.driver.find_element(by, selector)

    def find_all(self, selector, by=By.CSS_SELECTOR):
        """Find all elements matching selector."""
        return self.driver.find_elements(by, selector)

    def wait_for(self, selector, by=By.CSS_SELECTOR, timeout=10):
        """Wait for element to be present."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, selector)))

    def click(self, selector, by=By.CSS_SELECTOR):
        """Click element by selector."""
        element = self.wait_for(selector, by)
        element.click()
        return self

    def type(self, selector, text, by=By.CSS_SELECTOR):
        """Type text into element."""
        element = self.wait_for(selector, by)
        element.clear()
        element.send_keys(text)
        return self

    def screenshot(self, filepath):
        """Take screenshot and save to file."""
        self.driver.save_screenshot(filepath)
        return self

    def close(self):
        """Close browser."""
        self.driver.quit()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - automatically closes browser."""
        self.close()


# Example usage
if __name__ == "__main__":
    # Simple example
    with Browser() as browser:
        browser.goto("https://www.google.com")
        search_box = browser.find("textarea[name='q']")
        search_box.send_keys("Selenium Python")
        print("Browser opened and navigated to Google!")
        input("Press Enter to close browser...")
