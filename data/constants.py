# Класс, содержащий ссылки на страницы
class Constants:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'  # Главная страница
    REGISTER = BASE_URL + '/register'  # Страница регистрации - абсолюный путь
    REGISTER_RELATIVE = '/register'  # Страница регистрации - относительный путь
    LOGIN = BASE_URL + '/login'  # Страница логина - абсолютный путь
    LOGIN_RELATIVE = '/login'  # Страница логина - относительный путь
    ACCOUNT = '/account'  #  относиельный путь к аккаунта
    FORGOT_PASSWORD = BASE_URL + '/forgot-password' #  Страница восстановления пароля
    PROFILE = BASE_URL + '/account/profile'  # Страница редактирования профиля
    ORDERS = BASE_URL + '/feed'  # Страница Лента заказов
    ORDER_HISTORY = BASE_URL + '/order-history'  # Сраница истории заказов пользователя


# Класс, содержащий данные пользователей
class Users:
    USER_NAME = 'Автотест'  # Имя пользователя
    USER_EMAIL = 'auto-namo@tests.tests'  # Email пользователя
    USER_PASSWORD = 'Qwerty123'  # Пароль пользователя
    INVALID_PASSWORD = '123'  # Неправильный пароль пользователя
    USER_PASSWORD_HIDDEN = '*****'  # Скрытый пароль пользователя


# Класс, содержащий текст лейблов
class Labels:
    # Страница регистрации
    PASSWORD_ERROR = 'Некорректный пароль'
    REG_ERROR = 'Такой пользователь уже существует'

    # Логин
    LOGIN_TITLE = 'Вход'

    # Профиль пользователя
    PROFILE = "Профиль"
    ORDER_HISTORY = "История заказов"
    LOGOUT = "Выход"

    # Конструктор
    CONSTRUCTOR_TITLE = "Соберите бургер"
    CATEGORY_BUNS = "Булки"
    CATEGORY_SOUCES = "Соусы"
    CATEGORY_FILLING = "Начинки"
    ORDER_BUTTON = "Оформить заказ"
    ORDER_BUTTON_GUEST = "Войти в аккаунт"
