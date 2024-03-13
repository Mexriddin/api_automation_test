from utils.helper import Helper
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from services.users.models.user_model import UserModel
from config.headers import Headers
import requests
import allure


class UsersAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create a user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.created_user
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response=response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid=uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response=response.json())
        model = UserModel(**response.json())
        return model