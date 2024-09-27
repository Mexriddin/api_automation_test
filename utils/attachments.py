import requests_to_curl as curl
import json
import allure
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
