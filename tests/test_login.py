import pytest
from generator.data_gen import DataGenHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from data.constants import Constants, Users, Labels
from data.locators import Locators


class TestLogin:
    # Проверяем текст для незалогиненного пользователя на кнопке заказа на главной странице
    def test_login_from_homepage_button_text(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        button_text = driver.find_element(*Locators.ORDER_BUTTON).text
        assert button_text == Labels.ORDER_BUTTON_GUEST

    # проверяем логин с главной страницы
    def test_login_from_homepage(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ORDER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys(Users.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Users.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        button_text = driver.find_element(*Locators.ORDER_BUTTON).text
        assert button_text == Labels.ORDER_BUTTON

    # проверяем логин по клику на Личный кабинет в хидере
    def test_login_from_header(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.EMAIL).send_keys(Users.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Users.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        button_text = driver.find_element(*Locators.ORDER_BUTTON).text
        assert button_text == Labels.ORDER_BUTTON

    # проверяем логин из формы регистрации
    def test_login_from_registration_form(self, driver):
        driver.get(Constants.REGISTER)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_LINK))
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.EMAIL).send_keys(Users.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Users.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        button_text = driver.find_element(*Locators.ORDER_BUTTON).text
        assert button_text == Labels.ORDER_BUTTON

    # проверяем логин из формы восстановления пароля
    def test_login_from_forgot_password_form(self, driver):
        driver.get(Constants.FORGOT_PASSWORD)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_LINK))
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.EMAIL).send_keys(Users.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Users.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        button_text = driver.find_element(*Locators.ORDER_BUTTON).text
        assert button_text == Labels.ORDER_BUTTON




