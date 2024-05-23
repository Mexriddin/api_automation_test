import allure
import requests
import requests_to_curl as curl
import json
from allure_commons.types import AttachmentType


class Attachment:
    @classmethod
    def attach_request_body(cls, request_body):
        if request_body is not None:
            allure.attach(body=json.dumps(request_body, indent=4), name="API Request Body",
                          attachment_type=AttachmentType.JSON)

    @classmethod
    def attach_response(cls, response):
        try:
            response_data = response.json()
            allure.attach(body=json.dumps(response_data, indent=4), name="API Response",
                          attachment_type=AttachmentType.JSON)
        except json.decoder.JSONDecodeError:
            allure.attach(body=response.content, name="API Response", attachment_type=AttachmentType.TEXT)
            # assert False, f"Response is not JSON format. Response text is '{response.text}'"

    @classmethod
    def attach_curl(cls, response):
        curl_line = curl.parse(response, return_it=True, print_it=False)
        allure.attach(body=curl_line, name="cURL", attachment_type=AttachmentType.TEXT)


class SuperRequests:
    @staticmethod
    def post(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return SuperRequests._send(url, "POST", json_data, headers, cookies, params)

    @staticmethod
    def get(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return SuperRequests._send(url, "GET", json_data, headers, cookies, params)

    @staticmethod
    def put(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None,
            files: dict = None):
        return SuperRequests._send(url, "PUT", json_data, headers, cookies, params, files)

    @staticmethod
    def patch(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return SuperRequests._send(url, "PATCH", json_data, headers, cookies, params)

    @staticmethod
    def delete(url: str, json_data: dict = None, headers: dict = None, cookies: dict = None, params: dict = None):
        return SuperRequests._send(url, "DELETE", json_data, headers, cookies, params)

    @staticmethod
    def _send(url: str, method: str, json_data: dict, headers: dict, cookies: dict, params: dict, files: dict):
        with allure.step(f"{method} request to URL: {url}"):

            if headers is None:
                headers = {}
            if cookies is None:
                cookies = {}
            if params is None:
                params = {}
            if files is None:
                files = {}

            Attachment.attach_request_body(json_data)

            if method == "GET":
                response = requests.get(url, json=json_data, cookies=cookies, headers=headers, params=params)
            elif method == "POST":
                response = requests.post(url, json=json_data, cookies=cookies, headers=headers, params=params)
            elif method == "PUT":
                response = requests.put(url, json=json_data, cookies=cookies, headers=headers, params=params,
                                        files=files)
            elif method == "PATCH":
                response = requests.patch(url, json=json_data, cookies=cookies, headers=headers, params=params)
            elif method == "DELETE":
                response = requests.delete(url, json=json_data, cookies=cookies, headers=headers, params=params)
            else:
                raise Exception(f"Bad HTTP method '{method}' was received")

            Attachment.attach_response(response)
            Attachment.attach_curl(response)

            return response
