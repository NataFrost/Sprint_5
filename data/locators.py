from selenium.webdriver.common.by import By
from data.constants import Constants


class Locators:
    # Форма регистрации и логина
    NAME = (By.XPATH, ".//label[text()='Имя']/following::input")  # поле для ввода имени
    EMAIL = (By.XPATH, ".//label[text()='Email']/following::input")  # поле для ввода емейла (форма регистрации)
    PASSWORD = (By.XPATH, ".//input[@type='password']")  # поле ввода пароля (форма регистрации и входа)
    # локаторы кнопок одинаковые, но сделала два локатора на случай изменений, чтобы проще было изменить при необходимости
    REG_BUTTON = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button")  # кнопка (форма регистрации)
    LOGIN_LINK = (By.XPATH, f".//a[@href='{Constants.LOGIN_RELATIVE}']")  # ссылка для Входа для зарегистрированных пользоваелей на форме регистрации
    REG_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]")  # сообщение об ошибке на форме регистрации

    # Форма входа
    LOGIN = (By.XPATH, ".//label[text()='Логин']/following::input")  # поле для ввода логина (форма входа)
    LOGIN_BUTTON = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button")  # кнопка (форма входа)
    REG_LINK = (By.XPATH, f".//a[@href='{Constants.REGISTER_RELATIVE}']")  # ссылка для Новых пользователей на форме входа
    LOGIN_TITLE = (By.XPATH, ".//div[contains(@class, 'Auth_login')]//h2")  # название формы входа

    # Хидер
    MY_ACCOUNT = (By.XPATH, f".//a[@href='{Constants.ACCOUNT}']")  # Личный кабинет в хидере
    HEADER_NAV_ITEMS_LINKS = (By.XPATH, ".//ul[contains(@class, 'AppHeader')]//li//a")  # Ссылки в хидере (Конструктор, Лента заказов)
    LOGO = (By.XPATH, ".//div[contains(@class, 'logo')]//a")  # Логотип в хидере

    # Профиль пользователя
    PROFILE_NAV_ITEMS = (By.XPATH, ".//ul[contains(@class, 'Account_list')]//li")  # Пункты навигации по профилю
    PROFILE_NAV_ITEMS_LINKS = (By.XPATH, ".//ul[contains(@class, 'Account_list')]//li//a")  # Ссылки для навигации по профилю
    LOGOUT = (By.XPATH, ".//button[contains(@class, 'Account_button')]")  # Выход из аккаунта

    # Главная страница
    CONSTRUCTOR_TITLE = (By.TAG_NAME, "h1")  # Название главной страницы
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'totalContainer')]/following-sibling::button")  # Кнопка Оформить заказ

    CATEGORIES = (By.XPATH, ".//section[contains(@class, 'BurgerIngredients')]//div/div")  # Категории конструктора

    BUNS_CATEGORY = (By.XPATH, ".//section[contains(@class, 'BurgerIngredients')]//div[1]/div[1]")
    SAUCE_CATEGORY = (By.XPATH, ".//section[contains(@class, 'BurgerIngredients')]//div[1]/div[2]")
    FILLINGS_CATEGORY = (By.XPATH, ".//section[contains(@class, 'BurgerIngredients')]//div[1]/div[3]")

    BUNS_TITLE = (By.XPATH, ".//div[contains(@class, 'ingredients__menuContainer')]//h2[1]")  # Название секции "Булки"
    SAUCE_TITLE = (By.XPATH, ".//div[contains(@class, 'ingredients__menuContainer')]//h2[2]")  # Название секции "Соусы"
    FILLINGS_TITLE = (By.XPATH, ".//div[contains(@class, 'ingredients__menuContainer')]//h2[3]")  # Название секции "Начинки"

    CONTAINER = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients')]")  # область с ингридиентами на главной
