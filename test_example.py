"""
Example test file demonstrating Selenium + pytest integration.
Run with: pytest test_example.py -v
"""

import pytest
from browser import Browser


@pytest.fixture
def browser():
    """Fixture that provides a browser instance for each test."""
    browser_instance = Browser(headless=False)
    yield browser_instance
    browser_instance.close()


@pytest.mark.skip(reason="Google search test is flaky due to CAPTCHA and dynamic content")
def test_google_search(browser):
    """Test Google search functionality."""
    browser.goto("https://www.google.com")

    # Find and interact with search box
    search_box = browser.find("textarea[name='q']")
    assert search_box is not None

    search_box.send_keys("Python Selenium")
    search_box.submit()

    # Wait for results
    browser.wait_for("#search")

    # Verify results appeared
    results = browser.find_all(".g")
    assert len(results) > 0


def test_page_title(browser):
    """Test that page title is correct."""
    browser.goto("https://www.python.org")
    assert "Python" in browser.driver.title


def test_screenshot(browser, tmp_path):
    """Test screenshot functionality."""
    browser.goto("https://www.github.com")
    screenshot_path = tmp_path / "github_screenshot.png"
    browser.screenshot(str(screenshot_path))
    assert screenshot_path.exists()
