import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose your language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    try:
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome("d://1//chromedriver.exe", options=options)
    finally:
        pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()



