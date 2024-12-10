import pytest
from generator.data_gen import DataGenHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from data.constants import Constants, Users, Labels
from data.locators import Locators


class TestMyAccount:
    # проверяем, что имя пользователя правильное
    def test_my_profile_user_name(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.NAME))
        user_name = driver.find_element(*Locators.NAME).get_attribute("value")
        assert user_name == Users.USER_NAME

    # проверяем, что емейл пользователя правильный
    def test_my_profile_email(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN))
        user_name = driver.find_element(*Locators.LOGIN).get_attribute("value")
        assert user_name == Users.USER_EMAIL

    # проверяем, что пароль скрыт
    def test_my_profile_password(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PASSWORD))
        password = driver.find_element(*Locators.PASSWORD).get_attribute("value")
        assert password == Users.USER_PASSWORD_HIDDEN

    # проверяем количество разделов в профиле
    def test_my_profile_navigation_items_quantity(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        nav_items = driver.find_elements(*Locators.PROFILE_NAV_ITEMS)
        assert len(nav_items) == 3

    # проверяем имя раздела по умолчанию (Профиль)
    def test_my_profile_default_navigation_item_name(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        nav_item = driver.find_elements(*Locators.PROFILE_NAV_ITEMS)[0]
        assert nav_item.text == Labels.PROFILE

    # проверяем название раздела с заказами в профиле
    def test_my_profile_order_history_navigation_item_name(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        nav_item = driver.find_elements(*Locators.PROFILE_NAV_ITEMS)[1]
        assert nav_item.text == Labels.ORDER_HISTORY

    # проверяем, что по умолчанию активен раздель Профиль
    def test_my_profile_default_navigation_item_active(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        nav_item = driver.find_elements(*Locators.PROFILE_NAV_ITEMS_LINKS)[0].get_attribute("class")
        assert "Account_link_active" in nav_item

    # проверяем навигацию к Заказам в профиле - пункт навигации активен
    def test_my_profile_navigation_to_order_history(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        driver.find_elements(*Locators.PROFILE_NAV_ITEMS_LINKS)[1].click()
        nav_item = driver.find_elements(*Locators.PROFILE_NAV_ITEMS_LINKS)[1].get_attribute("class")
        assert "Account_link_active" in nav_item

    # проверяем навигацию из профиля в консруктор
    def test_my_profile_navigation_to_constructor(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        driver.find_elements(*Locators.HEADER_NAV_ITEMS_LINKS)[0].click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        title = driver.find_element(*Locators.CONSTRUCTOR_TITLE).text
        assert title == Labels.CONSTRUCTOR_TITLE

    # проверяем навигацию в конструктор по клику на логотип
    def test_my_profile_navigation_to_constructor_via_logo(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        title = driver.find_element(*Locators.CONSTRUCTOR_TITLE).text
        assert title == Labels.CONSTRUCTOR_TITLE

    # проверяем логаут
    def test_my_profile_logout_name(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        logout = driver.find_element(*Locators.LOGOUT).text
        assert logout == Labels.LOGOUT

    def test_my_profile_logout(self, driver, login):
        driver.find_element(*Locators.MY_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_NAV_ITEMS))
        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_TITLE))
        assert driver.current_url == Constants.LOGIN

