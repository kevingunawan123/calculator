import os

import pytest

RUN_SELENIUM = os.getenv("RUN_SELENIUM") == "1"
pytestmark = pytest.mark.skipif(
    not RUN_SELENIUM, reason="Set RUN_SELENIUM=1 to enable Selenium UI test."
)

if RUN_SELENIUM:
    import multiprocessing
    import time

    from app import app
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def live_server():
    if not RUN_SELENIUM:
        return

    def run_app():
        app.run(debug=False, use_reloader=False, port=5001)

    proc = multiprocessing.Process(target=run_app, daemon=True)
    proc.start()
    time.sleep(1.5)
    yield "http://127.0.0.1:5001/"
    proc.terminate()
    proc.join()


@pytest.fixture(scope="session")
def browser():
    if not RUN_SELENIUM:
        return
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_web_calculator_flow(live_server, browser):
    if not RUN_SELENIUM:
        return
    browser.get(live_server)
    browser.find_element(By.ID, "a").send_keys("2")
    browser.find_element(By.ID, "b").send_keys("3")
    browser.find_element(By.ID, "op").send_keys("add")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    body_text = browser.page_source
    assert "Result:" in body_text
    assert "5.0" in body_text
