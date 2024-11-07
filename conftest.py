import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    firefox_options = Options()
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    driver.fullscreen_window()
    yield driver
    driver.quit()
