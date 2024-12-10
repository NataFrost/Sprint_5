import random
import string


class DataGenHelper:
    def __init__(self):
        pass

    @staticmethod
    def random_email():
        domains = ["gmail.com", "yandex.ru", "mail.ru", "telekom.ru", "rambler.ru"]
        name_length = random.randint(5, 12)  # длина имени от 5 до 12 символов
        domain = random.choice(domains)
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
        return f"{name}@{domain}"

    @staticmethod
    def random_password():
        password_length = random.randint(6, 10)  # длина имени от 6 до 10 символов
        return ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
