import pytest
from generator.data_gen import DataGenHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.constants import Constants, Users, Labels
from data.locators import Locators


faker = DataGenHelper()


class TestRegistration:
    # проверка регистрации
    def test_registration(self, driver):
        driver.get(Constants.REGISTER)
        email = faker.random_email()
        password = faker.random_password()
        driver.find_element(*Locators.NAME).send_keys(Users.USER_NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK))
        assert driver.find_element(*Locators.LOGIN_TITLE).text == Labels.LOGIN_TITLE

    # проверка регистрации с неправильным (по формату) паролем
    def test_registration_invalid_password(self, driver):
        driver.get(Constants.REGISTER)
        email = faker.random_email()
        password = Users.INVALID_PASSWORD
        driver.find_element(*Locators.NAME).send_keys(Users.USER_NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_ERROR))
        error_text = driver.find_element(*Locators.REG_ERROR).text
        assert error_text == Labels.PASSWORD_ERROR

    # проверка повторной регистрации с уже зарегистрированной почтой
    def test_registration_existing_email(self, driver):
        driver.get(Constants.REGISTER)
        driver.find_element(*Locators.NAME).send_keys(Users.USER_NAME)
        driver.find_element(*Locators.EMAIL).send_keys(Users.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Users.USER_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_ERROR))
        error_text = driver.find_element(*Locators.REG_ERROR).text
        assert error_text == Labels.REG_ERROR

    # проверка, что созданный пользователь может залогиниться
    def test_login_with_newly_created_user(self, driver):
        driver.get(Constants.REGISTER)
        email = faker.random_email()
        password = faker.random_password()
        driver.find_element(*Locators.NAME).send_keys(Users.USER_NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        button_text = driver.find_element(*Locators.ORDER_BUTTON).text
        assert button_text == Labels.ORDER_BUTTON


