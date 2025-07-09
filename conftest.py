import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# -------------------------------
# Fixture: WebDriver Setup/Teardown
# -------------------------------

@pytest.fixture
def driver():
    path = ChromeDriverManager().install()
    print(f"Resolved ChromeDriver path: {path}")  # DEBUG
    if not path.endswith("chromedriver"):
        raise RuntimeError(f"Unexpected driver path: {path}")
    service = Service(path)
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")  # Headless is important for CI
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# -------------------------------
# Hook: Screenshot on Test Failure
# -------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join("screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(filepath)