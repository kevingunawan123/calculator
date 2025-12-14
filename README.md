# Mini Python Project with GitHub Actions CI

This repo contains a tiny Python module plus tests to demonstrate how to wire up GitHub Actions for linting and testing.

## Project layout
- `app.py` – Flask app that exposes the calculator in the browser.
- `templates/index.html` – HTML template for the web calculator UI.
- `src/calculator.py` – simple math helpers we will test.
- `tests/test_calculator.py` – pytest suite that exercises the helpers.
- `tests/test_app.py` – tests for the Flask endpoints.
- `tests/test_selenium.py` – optional Selenium UI smoke test (skipped unless enabled).
- `features/` – behave BDD scenarios and steps.
- `locustfile.py` – Locust load-test entrypoint.
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

## Optional testing types

### BDD (behave)
- Install deps (already in `requirements.txt`), then run from repo root:
  ```bash
  behave
  ```
- Scenarios live in `features/calculator.feature`; steps are in `features/steps/` and use Flask's test client (no live server needed).

### Load testing (Locust)
- Start the app in another terminal: `python app.py`
- In a new shell, run:
  ```bash
  locust -f locustfile.py --host=http://127.0.0.1:5000
  ```
- Open the URL Locust prints (default http://localhost:8089), set user count/spawn rate, and start the test.

### UI smoke (Selenium, optional)
- Requires Chrome/Chromium available on your machine. The test is skipped unless you opt in.
- Start the app in another terminal (if not using the embedded fixture): `python app.py`
- Run with opt-in flag:
  ```bash
  RUN_SELENIUM=1 pytest tests/test_selenium.py
  ```
- The test spins up a headless Chrome via `webdriver-manager`, fills the form, and asserts the result. Skip in CI unless your runner has a browser.

CI note: GitHub Actions has a separate `selenium` job that sets `RUN_SELENIUM=1` on Ubuntu with headless Chrome. It depends on the main `build` job. If you do not want Selenium in CI, remove or disable that job in `.github/workflows/ci.yml`.

## How the GitHub workflow works
- Triggers on pushes and pull requests to `main`.
- Matrix builds on Python 3.10 and 3.11.
- Steps:
  1. Check out the code.
  2. Set up the requested Python version.
  3. Install dependencies from `requirements.txt`.
  4. Run formatting/lint (here we use `python -m compileall` as a lightweight syntax check) and `pytest`.
- If any step fails, the workflow marks the check as failed so you see it in the PR.
