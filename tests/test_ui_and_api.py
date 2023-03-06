import pytest
import requests

from data.locators import MainPage, URLSwagger
from helper.helper import DataGenerator
from helper.url_api import BaseURL, URL
from schemas.json_schemas import JsonSheme


class TestUI:
    @pytest.mark.parametrize('schema, index_ui_end_point', [(JsonSheme().register_post(), 11),
                                                            (JsonSheme().register_post_bad_request(), 12)])
    def test_checking_handles_post(self, browser, schema, index_ui_end_point):
        browser.scroll_to_element(1000, browser.get_element_by_class(MainPage.main_header))
        browser.click(browser.get_element_by_data_key_index(MainPage.endpoint, index_ui_end_point))
        response = requests.post((BaseURL.base_url + URL.register), json=schema)
        actual_status_code_ui = browser.get_element_by_data_key_index(MainPage.response_code, 1).text
        actual_response_ui = browser.get_element_by_data_key_index(MainPage.output_response, 1).text
        actual_response_api = response.text
        splitter_ui = DataGenerator().splitter(actual_response_ui)
        splitter_api = DataGenerator().splitter(actual_response_api)
        browser.get_element_by_text(MainPage.some_text)
        assert splitter_ui == splitter_api
        assert actual_status_code_ui == str(response.status_code)

    @pytest.mark.parametrize('url, index_ui_end_point', [(URL.list_users, 1),
                                                         (URL.single_users, 2),
                                                         (URL.single_users_not_found, 3),
                                                         (URL.list_resourse, 4),
                                                         (URL.single_resourse, 5),
                                                         (URL.single_resourse_not_found, 6),
                                                         (URL.delay, 15)])
    def test_checking_handles_get(self, browser, url, index_ui_end_point):
        browser.scroll_to_element(1000, browser.get_element_by_class(MainPage.main_header))
        browser.click(browser.get_element_by_data_key_index(MainPage.endpoint, index_ui_end_point))
        response = requests.get(BaseURL.base_url + url)
        response1 = response.text
        actual_status_code_ui = browser.get_element_by_data_key_index(MainPage.response_code, 1).text
        actual_response_ui = browser.get_element_by_data_key_index(MainPage.output_response, 1).text
        splitter_ui = DataGenerator().splitter(actual_response_ui)
        splitter_api = DataGenerator().splitter(response1)
        browser.get_element_by_text(MainPage.some_text)
        assert splitter_ui == splitter_api
        assert actual_status_code_ui == str(response.status_code)

    def test_checking_operation_request_buttons(self, browser):
        assert browser.check_elements_displayed(browser.get_element_by_text(MainPage.fake_data_text),
                                                browser.get_element_by_text(MainPage.real_responses_text),
                                                browser.get_element_by_text(MainPage.always_on_text))

        browser.scroll_to_element(800, browser.get_element_by_class(MainPage.main_header))

        assert browser.amount_of_elements_by_data_key(MainPage.endpoint) == 15

    def test_contribution(self, browser):
        browser.execute_scripts(MainPage.scroll_down)
        browser.send_value_by_input(MainPage.send_keys_field, MainPage.text)
        assert browser.get_element_by_text(MainPage.breathe).is_enabled()

    def test_move_another_page(self, browser):
        browser.execute_scripts(MainPage.scroll_down)
        browser.scroll_to_element(-1000, browser.get_element_by_class(MainPage.window_endpoint_class))
        browser.click((browser.locator_value_to_tuple(MainPage.swagger_button)))
        assert browser.switch_tab_and_check_url(URLSwagger.swagger_url)

