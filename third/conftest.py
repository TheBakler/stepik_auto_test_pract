import pytest
import json
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def load_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
        return config
