# CI/CD Setup Guide

## ✅ What's Been Configured

Your project now has a complete GitHub Actions CI/CD pipeline with:

### 1. **Code Quality Checks** (lint job)
- Black formatting validation
- Flake8 linting for code standards
- Runs on every push and PR

### 2. **Automated Tests** (test job)
- Runs pytest tests in headless Chrome
- Generates coverage reports
- Uploads to Codecov (optional)

### 3. **Integration Tests** (integration-test job)
- Tests with Docker Compose services
- Validates login flows
- Gracefully skips if Docker images unavailable

## 📁 Files Created

```
.github/workflows/ci.yml    # Main CI workflow
.gitignore                   # Python/IDE/testing ignores
.flake8                      # Linting configuration
pytest.ini                   # Pytest configuration
requirements-dev.txt         # Development dependencies
CI_CD_SETUP.md              # This file
```

## 🚀 Next Steps

### 1. Create GitHub Repository
```bash
# Create a new repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/selenium-dev-setup.git
git push -u origin main
```

### 2. Enable GitHub Actions
- Go to your repo → **Settings** → **Actions** → **General**
- Enable "Allow all actions and reusable workflows"

### 3. Set Up Branch Protection (Optional)
- Go to **Settings** → **Branches** → **Add rule**
- Branch name pattern: `main`
- Check "Require status checks to pass before merging"
- Select: `Code Quality`, `Tests`

### 4. Install Dev Dependencies Locally
```bash
source venv/bin/activate
pip install -r requirements-dev.txt
```

### 5. Format Your Code
```bash
# Auto-format all Python files
black .

# Check formatting without changes
black --check .
```

### 6. Run Linting Locally
```bash
# Check for errors
flake8 .
```

## 🎯 Workflow Triggers

The CI pipeline runs on:
- **Push** to `main` or `develop` branches
- **Pull requests** to `main` or `develop`
- **Manual trigger** (via GitHub Actions UI)

## 📊 Coverage Reports (Optional)

To enable Codecov:
1. Sign up at https://codecov.io
2. Connect your GitHub repository
3. Add `CODECOV_TOKEN` to repo secrets (Settings → Secrets → Actions)

## 🧪 Local Testing Commands

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest test_example.py -v

# Run in headless mode (like CI)
pytest test_example.py -v --headless
```

## 🔧 Customization

### Modify Python Version
Edit `.github/workflows/ci.yml`:
```yaml
python-version: '3.11'  # Change to 3.9, 3.10, 3.12, etc.
```

### Add More Branches to CI
```yaml
on:
  push:
    branches: [ main, develop, staging ]  # Add more branches
```

### Adjust Linting Rules
Edit `.flake8` to change max line length, ignore rules, etc.

### Run Tests on Multiple Python Versions
Add matrix strategy to workflow:
```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11', '3.12']
```

## 📝 Pre-commit Hooks (Optional)

To run checks before every commit:

```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
EOF

# Install hooks
pre-commit install
```

## 🐛 Troubleshooting

### Tests fail in CI but pass locally
- Ensure headless mode works: `pytest --headless`
- Check Chrome version compatibility
- Verify all dependencies in `requirements.txt`

### Linting fails
```bash
# Auto-fix formatting
black .

# Check what flake8 complains about
flake8 . --show-source
```

### Docker integration tests don't run
- The workflow checks for Docker images first
- If images don't exist, tests are skipped gracefully
- Build your Docker images before pushing

## 📚 Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Linting](https://flake8.pycqa.org/)
