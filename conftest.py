import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.constants import Constants, Users
from data.locators import Locators


# инициализация браузера
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


# авторизация пользователя
@pytest.fixture
def login(driver):
    driver.get(Constants.LOGIN)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK))
    driver.find_element(*Locators.EMAIL).send_keys(Users.USER_EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Users.USER_PASSWORD)
    driver.find_element(*Locators.REG_BUTTON).click()
    return driver
