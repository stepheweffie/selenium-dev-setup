# Selenium Dev Setup

[![CI](https://github.com/stepheweffie/selenium-dev-setup/actions/workflows/ci.yml/badge.svg)](https://github.com/stepheweffie/selenium-dev-setup/actions/workflows/ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)

A development-ready Selenium environment with Chrome browser automation, complete with CI/CD pipeline.

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

## CI/CD

This project includes a complete GitHub Actions pipeline:

- **Code Quality**: Black formatting + Flake8 linting
- **Automated Tests**: Pytest with headless Chrome
- **Integration Tests**: Docker Compose service testing

See [CI_CD_SETUP.md](CI_CD_SETUP.md) for full documentation.

### Local Quality Checks

```bash
# Format code
black .

# Lint code
flake8 .

# Run tests in CI mode
CI=true pytest -v
```

## Requirements

- Python 3.7+
- Chrome browser installed
- ChromeDriver (managed automatically by webdriver-manager)
