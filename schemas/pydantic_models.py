from pydantic import BaseModel, validator

from typing import List, Dict


class RegisterPost(BaseModel):
    token: str

    @classmethod
    @validator("token")
    def check_length_token(cls, token):
        if len(token) <= 10:
            raise ValueError("token length is not sufficient")
        else:
            return token


class FirstGetDataList(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class ListUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[FirstGetDataList]
    support: Dict[str, str]


class SingleUsers(BaseModel):
    data: Dict[str, str]
    support: Dict[str, str]


class ListResourse(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class Resourse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ListResourse]
    support: Dict[str, str]


class SingleResourse(BaseModel):
    data: dict
    support: dict


class JobUserPost(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class JobUserPutPatch(BaseModel):
    name: str
    job: str
    updatedAt: str
