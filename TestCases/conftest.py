from pytest_metadata.plugin import metadata_key
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="Browser to run tests: Chrome, Firefox, or Ie")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = Chrome()
        print("Launching Chrome browser")
    elif browser == 'Firefox':
        driver = Firefox()
        print("Launching Firefox browser")
    elif browser == 'Ie':
        driver = Ie()
        print("Launching Internet Explorer browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()


def pytest_configure(config):
    config.stash[metadata_key]["foo"] = "bar"

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["foo"] = "bar"



