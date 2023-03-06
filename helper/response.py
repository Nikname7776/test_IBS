class Responses:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code
        self.response_json = response.json()

    def check_status_code(self, status_code: int) -> int:
        """Метод проверки статус кода"""
        return self.response_status == status_code

    def validate_json_schemas(self, schema):
        """Метод для валидации json"""
        schema.parse_obj(self.response_json)

    def get_json_word(self, field_name: str) -> bool:
        """Метод для получения поля"""
        check = self.response.json()
        check_info = check.get(field_name)
        return check_info

    def get_text(self) -> str:
        """Метод для получения данных в виде текста"""
        response = self.response.text
        return response
