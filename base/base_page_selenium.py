from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePageObject(object):
    """Класс, предоставляющий базовые методы для работы с веб-элементами."""

    def __init__(self, driver):
        self.driver = driver

    def wait_located(self, locator) -> WebElement:
        """
        Ожидает появление элемента на странице и возвращает его.

        :param locator: Кортеж, с методом поиска и локатором элемента.
        """
        return WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(locator)
        )

    def find_elements(self, by: By, locator: str) -> List[WebElement]:
        """
        Возвращает список элементов DOM, если не находит, то возвращает ошибку.


        :param locator: Кортеж, с методом поиска и локатором элемента.
        :param by: Стратегия поиска.
        """
        return self.driver.find_elements(by, locator)

    def element_clickable(self, locator: tuple or WebElement) -> WebElement:
        """
        Ожидает кликабельности элемента и возвращает его.

        :param locator: Кортеж, с методом поиска и локатором элемента или WebElement.
        """
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator)
        )

    def click(self, locator: tuple or WebElement) -> None:
        """
        Кликает по элементу на странице.

        :param locator: Кортеж, с методом поиска и локатором элемента.
        """
        if isinstance(locator, tuple):
            self.element_clickable(locator).click()
        else:
            locator.click()

    @staticmethod
    def check_elements_displayed(*elements: WebElement) -> bool:
        """
        Проверяет наличие элементов на странице.

        param: elements: Итерируемый объект
        """
        for elem in elements:
            if not elem.is_displayed():
                return False
        return True

    def execute_scripts(self, script: str, *args):
        """Метод позволяющий использовать скрипты js.

        param: script: Скрипт js."""

        self.driver.execute_script(script, *args)

    @staticmethod
    def locator_value_to_tuple(locator_value: str) -> tuple:
        """Преобразует значение локатора в кортеж с методом поиска - XPATH.

        param: locator_value: Значение локатора.
        """
        return By.CSS_SELECTOR, locator_value

    def switch_tab_and_check_url(self, url: str) -> bool:
        """
        Переключает драйвер на вкладку по заданному адресу страницы.

        :param url: Заданный адрес страницы.
        :return: True, если переключение удалось. Иначе, False.
        """
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if url in self.driver.current_url:
                return True
        return False
