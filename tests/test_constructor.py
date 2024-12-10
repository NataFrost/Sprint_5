from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.constants import Constants, Labels
from data.locators import Locators
from framework.base import BaseHelper
from framework.waits import WaitsHelper


class TestConstructor:

    # проверяем дефолтную категорию при открытии консруктора (Булки)
    def test_constructor_category_default(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CATEGORIES))
        default_category = driver.find_element(*Locators.BUNS_CATEGORY).get_attribute("class")
        assert "type_current" in default_category

    # проверяем имя дефолтной категории
    def test_constructor_category_default_name(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CATEGORIES))
        default_category = driver.find_element(*Locators.BUNS_CATEGORY).text
        assert Labels.CATEGORY_BUNS == default_category

    # проверяем переключение на раздел Соусы
    def test_constructor_go_to_category_sauce(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CATEGORIES))
        sauce_cat = driver.find_element(*Locators.SAUCE_CATEGORY)
        sauce_cat.click()
        current_category = driver.find_element(*Locators.SAUCE_CATEGORY).get_attribute("class")
        assert "type_current" in current_category

    # проверяем переключение на раздел Начинки
    def test_constructor_go_to_category_fillings(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CATEGORIES))
        fillings_cat = driver.find_element(*Locators.FILLINGS_CATEGORY)
        fillings_cat.click()
        current_category = driver.find_element(*Locators.FILLINGS_CATEGORY).get_attribute("class")
        assert "type_current" in current_category

    # проверяем, что при скролле контейнера меняется активная категория - Начинки
    def test_constructor_scroll_to_fillings(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONTAINER))
        fillings_cat_title = driver.find_element(*Locators.FILLINGS_TITLE)
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_cat_title)
        current_category = driver.find_element(*Locators.FILLINGS_CATEGORY).get_attribute("class")
        assert "type_current" in current_category

    # проверяем, что при скролле контейнера меняется активная категория - Соусы
    def test_constructor_scroll_to_sauces(self, driver):
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONTAINER))
        sauce_cat_title = driver.find_element(*Locators.SAUCE_TITLE)
        driver.execute_script("arguments[0].scrollIntoView(true);", sauce_cat_title)
        current_category = driver.find_element(*Locators.SAUCE_CATEGORY).get_attribute("class")
        assert "type_current" in current_category

    # проверяем, что при клике на категорию Начинки контейнер прокручиваеся до секции с Начинками
    def test_constructor_category_title_is_visible(self, driver):
        # объект для вспомогательных функций
        helper = BaseHelper(driver)
        # объект с пользовательскими ожиданиями
        waiter = WaitsHelper(driver)
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CATEGORIES))
        fillings_cat = driver.find_element(*Locators.FILLINGS_CATEGORY)
        fillings_cat.click()
        # определяем элемент с ингредиентами
        container = driver.find_element(*Locators.CONTAINER)
        fillings_cat_title = driver.find_element(*Locators.FILLINGS_TITLE)
        # ждем пока название секции Начинки прокрутится наверх
        waiter.wait_for_element_position_y(Locators.FILLINGS_TITLE, 300)
        # проверяем, что название наверху в видимой зоне контейнера
        assert helper.check_element_visibility(container, fillings_cat_title)

    # проверяем, что при клике на категорию Соусы контейнер прокручиваеся до секции с Соусами
    def test_constructor_category_title_is_visible(self, driver):
        # объект для вспомогательных функций
        helper = BaseHelper(driver)
        # объект с пользовательскими ожиданиями
        waiter = WaitsHelper(driver)
        driver.get(Constants.BASE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CATEGORIES))
        fillings_cat = driver.find_element(*Locators.SAUCE_CATEGORY)
        fillings_cat.click()
        # определяем элемент с ингредиентами
        container = driver.find_element(*Locators.CONTAINER)
        fillings_cat_title = driver.find_element(*Locators.SAUCE_TITLE)
        # ждем пока название секции Соусы прокрутится наверх
        waiter.wait_for_element_position_y(Locators.SAUCE_TITLE, 300)
        # проверяем, что название наверху в видимой зоне контейнера
        assert helper.check_element_visibility(container, fillings_cat_title)


