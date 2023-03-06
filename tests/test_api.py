import pytest
import requests

from helper.response import Responses
from helper.url_api import URL, BaseURL
from schemas.json_schemas import JsonSheme
from schemas.pydantic_models import ListUsers, SingleUsers, Resourse, SingleResourse, JobUserPost, JobUserPutPatch, \
    RegisterPost


class TestAPI:
    def test_list_users(self):
        response = Responses(requests.get(BaseURL.base_url + URL.list_users))
        response.validate_json_schemas(ListUsers)
        assert response.check_status_code(200)

    @pytest.mark.parametrize('url, status_code', [(URL.single_users, 200),
                                                  (URL.single_users_not_found, 404)])
    def test_single_user(self, url, status_code):
        response = Responses(requests.get(BaseURL.base_url + url))
        if response.check_status_code(200):
            response.validate_json_schemas(SingleUsers)
        assert response.check_status_code(status_code)

    @pytest.mark.parametrize('url, pydantic_modal, status_code',
                             [(URL.list_resourse, Resourse, 200),
                              (URL.single_resourse, SingleResourse, 200),
                              (URL.single_resourse_not_found, SingleResourse, 404)])
    def test_list_resourse(self, url, pydantic_modal, status_code):
        response = Responses(requests.get(BaseURL.base_url + url))
        if response.check_status_code(200):
            response.validate_json_schemas(pydantic_modal)
        assert response.check_status_code(status_code)

    @pytest.mark.parametrize('url, pydantic_modal, job, method, answer',
                             [(URL.users, JobUserPost, 'leader', requests.post, 201),
                              (URL.single_users, JobUserPutPatch, 'zion resident', requests.put, 200),
                              (URL.single_users, JobUserPutPatch, 'zion resident', requests.patch, 200)])
    def test_create_post(self, url, pydantic_modal, job, method, answer):
        response = Responses(method((BaseURL.base_url + url),
                                    json=JsonSheme().create_post(job)))
        response.validate_json_schemas(pydantic_modal)
        assert response.check_status_code(answer)

    def test_delete_users(self):
        response = requests.delete(BaseURL.base_url + URL.single_users)
        assert response.status_code == 204

    @pytest.mark.parametrize('schema, status_code',
                             [(JsonSheme().register_post(), 200),
                              (JsonSheme().register_post_bad_request(), 400)])
    def test_register_post(self, schema, status_code):
        response = Responses(requests.post((BaseURL.base_url + URL.register),
                                           json=schema))
        if response.check_status_code(200):
            response.validate_json_schemas(RegisterPost)
            assert response.get_json_word("id") == 4

        else:
            assert response.get_json_word("error") == "Missing password"
        assert response.check_status_code(status_code)

    @pytest.mark.parametrize('schema, status_code',
                             [(JsonSheme().login_post(), 200),
                              (JsonSheme().login_post_bad_request(), 400)])
    def test_login_post(self, schema, status_code):
        response = Responses(requests.post((BaseURL.base_url + URL.login),
                                           json=schema))
        if response.check_status_code(400):
            assert response.get_json_word("error") == "Missing password"
        assert response.check_status_code(status_code)

    def test_delayed_response(self):
        response = Responses(requests.get(BaseURL.base_url + URL.delay))
        response.validate_json_schemas(ListUsers)
        assert response.check_status_code(200)
