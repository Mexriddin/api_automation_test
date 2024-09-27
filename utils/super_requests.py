import allure
import requests
from utils.logger import Logger
from utils.attachments import Attachment


class SuperRequest:

    @staticmethod
    def post(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None,
             files: dict = None):
        return SuperRequest._send(url, "POST", json_data, headers, cookies, params, files)

    @staticmethod
    def get(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return SuperRequest._send(url, "GET", json_data, headers, cookies, params)

    @staticmethod
    def put(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None,
            files: dict = None):
        return SuperRequest._send(url, "PUT", json_data, headers, cookies, params, files)

    @staticmethod
    def patch(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return SuperRequest._send(url, "PATCH", json_data, headers, cookies, params)

    @staticmethod
    def delete(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return SuperRequest._send(url, "DELETE", json_data, headers, cookies, params)

    @classmethod
    def _send(cls, url: str, method: str, json_data: dict = None, headers: dict = None,
              cookies: dict = None, params: dict = None, files: dict = None):
        with allure.step(f"{method} request to URL: {url}"):
            Logger.add_request(url=url, method=method, data=json_data, headers=headers, cookies=cookies, params=params)
            Attachment.attach_request_body(json_data)

            response = requests.request(method=method, url=url, json=json_data, headers=headers, cookies=cookies,
                                        params=params, files=files)

            Logger.add_response(response=response)
            Attachment.attach_response(response)
            Attachment.attach_curl(response)
            return response