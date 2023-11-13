import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture
def driver():
        service = GeckoDriverManager().install()
        browser = webdriver.Firefox(service=Service(service))
        yield browser
        browser.quit()

