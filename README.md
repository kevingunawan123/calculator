# Mini Python Project with GitHub Actions CI

This repo contains a tiny Python module plus tests to demonstrate how to wire up GitHub Actions for linting and testing.

## Project layout
- `app.py` – Flask app that exposes the calculator in the browser.
- `templates/index.html` – HTML template for the web calculator UI.
- `src/calculator.py` – simple math helpers we will test.
- `tests/test_calculator.py` – pytest suite that exercises the helpers.
- `tests/test_app.py` – tests for the Flask endpoints.
- `.github/workflows/ci.yml` – CI pipeline that installs dependencies and runs linting/tests on every push and pull request.

## Running locally
1) Create a virtualenv and install dependencies:
   ```bash
   python -m venv .venv
   .venv/Scripts/activate  # on Windows; use .venv/bin/activate on macOS/Linux
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
2) Run the web app:
   ```bash
   python app.py
   ```
   Then open http://127.0.0.1:5000/ in your browser.
3) Run the tests:
   ```bash
   pytest
   ```

## How the GitHub workflow works
- Triggers on pushes and pull requests to `main`.
- Matrix builds on Python 3.10 and 3.11.
- Steps:
  1. Check out the code.
  2. Set up the requested Python version.
  3. Install dependencies from `requirements.txt`.
  4. Run formatting/lint (here we use `python -m compileall` as a lightweight syntax check) and `pytest`.
- If any step fails, the workflow marks the check as failed so you see it in the PR.
