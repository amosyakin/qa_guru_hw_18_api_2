import pytest
from selene import browser


@pytest.fixture(scope='session')
def base_url():
    return 'https://demowebshop.tricentis.com'


@pytest.fixture(scope='session', autouse=True)
def browser_setup(base_url):
    browser.config.base_url = base_url
    browser.config.window_width = 1024
    browser.config.window_height = 768

    yield

    browser.close()
