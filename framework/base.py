class BaseHelper:
    def __init__(self, driver):
        self.driver = driver

    # функция для проверки координат объекта в заданной области
    def check_element_visibility(self, container, element):
        bounding_rect = self.driver.execute_script("""
                    var element = arguments[0];
                    var rect = element.getBoundingClientRect();
                    return {
                        x: rect.x,
                        y: rect.y,
                        top: rect.top,
                        left: rect.left,
                        bottom: rect.bottom,
                        right: rect.right,
                        width: rect.width,
                        height: rect.height
                    };
                """, container)

        rect = element.rect
        viewport_x = bounding_rect['x']
        viewport_y = bounding_rect['y']
        viewport_width = bounding_rect['width']
        viewport_height = bounding_rect['height']

        # Проверка, виден ли элемент в области container
        if (rect['x'] >= viewport_x and
                rect['y'] >= viewport_y and
                rect['y'] + rect['height'] <= (viewport_y + viewport_height) and
                rect['x'] + rect['width'] <= (viewport_x + viewport_width)):
            # дополнительная проверка, что элемент промотался наверх контейнера
            if rect['y'] - viewport_y <= 70:
                return True
        else:
            return False
