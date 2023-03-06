import requests


class HttpMethods:
    cookies = ''

    def __init__(self):
        self.request = requests

    def get(self, url, body='', headers=''):
        return self.request.get(url,
                                json=body,
                                headers=headers,
                                cookies=self.cookies)
