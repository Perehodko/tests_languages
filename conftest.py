import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="chrome", help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    options = Options()
    #prefs = "ru"
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    time.sleep(30)
    #browser.quit()


