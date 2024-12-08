from ssl import Options
from selenium import webdriver
from selenium.webdriver import *

import pytest


@pytest.fixture(scope="session")
def driver():
    browser = "chrome"

    driver_options = Options()
    driver_options.add_argument("--headless")
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--disable-dev-shm-usage")

    if browser == "chrome":
        service = ChromeService()
        driver = webdriver.Chrome(service=service, driver_options=driver_options)
    elif browser == "firefox":
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, driver_options=driver_options)
    else:
        raise ValueError(f"{browser} is not supported.")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()