from dataclasses import dataclass


@dataclass
class BaseURL:
    base_url = 'https://reqres.in/api/'


@dataclass
class URL:
    list_users: str = 'users?page=2'
    single_users: str = 'users/2'
    single_users_not_found: str = 'users/23'
    list_resourse: str = 'unknown'
    single_resourse: str = 'unknown/2'
    single_resourse_not_found: str = 'unknown/23'
    users: str = 'users'
    register: str = 'register'
    login: str = 'login'
    delay: str = 'users?delay=3'
