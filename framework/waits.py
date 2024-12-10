from selenium.webdriver.support.ui import WebDriverWait


class WaitsHelper:
    def __init__(self, driver):
        self.driver = driver

    # Ожидание координаты y
    def wait_for_element_position_y(self, locator, expected_y, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).location['y'] <= expected_y,
            message=f"Элемент не достиг координаты y={expected_y}"
        )


