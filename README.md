# Selenium Dev Setup

A development-ready Selenium environment with Chrome browser automation.

## Setup

1. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Dependencies are already installed:**
   - selenium
   - webdriver-manager (auto-manages ChromeDriver)
   - pytest & pytest-selenium

## Usage

### Basic Browser Usage

```python
from browser import Browser

# Using context manager (auto-closes)
with Browser() as browser:
    browser.goto("https://example.com")
    browser.click("#button-id")
    browser.type("#input-field", "Hello World")
    browser.screenshot("screenshot.png")

# Or manual management
browser = Browser(headless=False)
browser.goto("https://example.com")
browser.close()
```

### Browser Options

```python
# Headless mode (no GUI)
browser = Browser(headless=True)

# Custom window size
browser = Browser(window_size=(1280, 720))
```

### Available Methods

- `goto(url)` - Navigate to URL
- `find(selector)` - Find single element (CSS selector by default)
- `find_all(selector)` - Find all matching elements
- `wait_for(selector, timeout=10)` - Wait for element to appear
- `click(selector)` - Click element
- `type(selector, text)` - Type into input field
- `screenshot(filepath)` - Save screenshot
- `close()` - Close browser

### Running Tests

```bash
# Run all tests
pytest test_example.py -v

# Run specific test
pytest test_example.py::test_google_search -v

# Run in headless mode
pytest test_example.py -v --headless
```

### Quick Test

Run the browser module directly to test Chrome setup:
```bash
python browser.py
```

## Development Tips

- Access raw Selenium driver: `browser.driver`
- Access WebDriverWait: `browser.wait`
- Use `By` for different selectors: `By.ID`, `By.XPATH`, `By.CLASS_NAME`, etc.

## Requirements

- Python 3.7+
- Chrome browser installed
- ChromeDriver (managed automatically by webdriver-manager)
