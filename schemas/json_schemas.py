
class JsonSheme:
    @staticmethod
    def create_post(job: str):
        return {
            "name": "morpheus",
            "job": job
        }

    @staticmethod
    def register_post():
        return {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

    @staticmethod
    def register_post_bad_request():
        return {
            "email": "sydney@fife"
        }

    @staticmethod
    def login_post():
        return {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

    @staticmethod
    def login_post_bad_request():
        return {
            "email": "peter@klaven"
        }
