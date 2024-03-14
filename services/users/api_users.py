from utils.helper import Helper
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from services.users.params import Params
from services.users.models.user_model import UserModel, UsersModel
from config.headers import Headers
import requests
import allure


class UsersAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()

    @allure.step("Create a user")
    def create_user(self):
        json_data = self.payloads.create_user()
        self.attach_request_body(json_data)
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=json_data
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response=response)
        model = UserModel(**response.json())
        return model

    @allure.step("Update user by ID")
    def update_user_by_id(self, uuid):
        json_data = self.payloads.create_user()
        self.attach_request_body(request_body=json_data)
        response = requests.patch(
            url=self.endpoints.update_user_by_id(uuid=uuid),
            headers=self.headers.basic,
            json=json_data
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response=response)
        model = UserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid=uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response=response)
        model = UserModel(**response.json())
        return model

    @allure.step("Delete user by ID")
    def delete_user_by_id(self, uuid):
        response = requests.delete(
            url=self.endpoints.delete_user_by_id(uuid=uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 204, response.json()
        self.attach_response(response=response)



    @allure.step("Get all users")
    def get_all_users(self, offset, limit):
        response = requests.get(
            url=self.endpoints.get_users_list,
            headers=self.headers.basic,
            params=self.params.user_list_params(offset=offset, limit=limit)
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response=response)
        model = UsersModel(**response.json())
        return model