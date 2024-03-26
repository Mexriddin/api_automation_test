import allure
import curl
import json
from allure_commons.types import AttachmentType


class Helper:

    def attach_request_body(self, request_body):
        allure.attach(body=json.dumps(request_body, indent=4), name="API Request Body",
                      attachment_type=AttachmentType.JSON)

    def attach_response(self, response):
        try:
            response_data = response.json()
            allure.attach(body=json.dumps(response_data, indent=4), name="API Response", attachment_type=AttachmentType.JSON)
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"


    def attach_curl(self, response):
        curl_line = curl.parse(response, return_it=True)
        allure.attach(body=curl_line, name="cURL", attachment_type=AttachmentType.TEXT)
