import os

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import utils.attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = '120'
def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        choices=['99', '100', '113', '114', '120', '121', '122', '123', '124', '125'],
        default='120'
    )
@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def browser_management(request):
    browser_version = request.config.getoption('--browser')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    # options.page_load_strategy = 'eager'
    browser.driver.fullscreen_window()

    yield

    utils.attach.add_screenshot(browser)
    utils.attach.add_logs(browser)
    utils.attach.add_html(browser)
    utils.attach.add_video(browser)
    browser.quit()