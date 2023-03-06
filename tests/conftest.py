import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from helper.layers import WorkWithElement


@pytest.fixture(scope='class')
def driver(background=False):
    chrome_options = Options()
    if background:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-gpu")
    else:
        print('___')
    web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='function')
def browser(driver):
    driver.get("https://reqres.in/")
    return WorkWithElement(driver)
