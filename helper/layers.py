from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from base.base_page_selenium import BasePageObject


class WorkWithElement(BasePageObject):

    """
    Класс, представляющий методы работы с веб-элементами.
    """
    data_key_index = "//*[@data-key='{}'][{}]"
    data_key = "//*[@data-key='{}']"
    text_in_class = "//*[@class='{}']"
    text_in_page = "//*[text()='{}']"
    css_selector_name = "[name='{}']"

    def get_element_by_data_key_index(self, element_text: str,  index: int) -> WebElement:
        """Возвращает WebElement у которого аттрибут data-key.

        param: element_text: Значение аттрибута элемента.
        param: index: Индекс элемента.
        """
        return self.wait_located((By.XPATH, self.data_key_index.format(element_text, index)))

    def amount_of_elements_by_data_key(self, element_text: str) -> int:
        """Возвращает WebElement у которого аттрибут data-key по индексу.

        param: attribute_value: Значение аттрибута элемента.
        """
        return len(self.find_elements(By.XPATH, self.data_key.format(element_text)))

    def get_element_by_class(self, element_text: str) -> WebElement:
        """Возвращает WebElement у которого аттрибут data-key.

        param: attribute_value: Значение аттрибута элемента.
        """
        return self.wait_located((By.XPATH, self.text_in_class.format(element_text)))

    def get_element_by_text(self, element_text: str) -> WebElement:
        """Проверяет наличие определенного текста на странице.

         param: element_text: Значение аттрибута текста.
         """
        return self.wait_located((By.XPATH, self.text_in_page.format(element_text)))

    def send_value_by_input(self, name: str, text: str) -> None:
        """Вставляет текст в input поле с аттрибутом родителя name.

        param: name: атрибут CSS_selector.
        param: text: текст для вставки.
        """
        self.wait_located((By.CSS_SELECTOR, self.css_selector_name.format(name))).send_keys(text)

    def click_element_by_data_key(self, element_text: str, index: int) -> None:
        """Кликает по тексту, который находится в data_key.

        param: element_text: Значение аттрибута элемента.
        """
        element = self.wait_located((By.XPATH, self.data_key_index.format(element_text, index)))
        self.element_clickable(element)
        element.click()

    def scroll_to_element(self, pixels: int, locator: WebElement, count=-10) -> None:
        """
        Эмулируeт прокрутку мышью ОТ заданного элемента на кол-во пикселей.

        :param locator: WebElement
        :param pixels: количество пикселей для смещения вниз.
        :param count: Коэффициент увеличения
        """
        scroll_origin = ScrollOrigin.from_element(locator, 0, count)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, pixels).perform()

