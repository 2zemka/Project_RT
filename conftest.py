import time
import pytest
from selenium import webdriver
from faker import Faker


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome('Chrome_driver/chromedriver.exe')
    driver.get("https://b2c.passport.rt.ru")

    yield driver
    driver.quit()

