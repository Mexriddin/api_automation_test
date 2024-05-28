from services.carts.endpoints import Endpoints
from config.headers import Headers
from services.carts.payloads import Payloads
from services.carts.models.cart_models import CartModel
from utils.super_requests import SuperRequests as super_requests
import allure


class CartAPI:
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step("Get user's cart by UUID")
    def get_cart(self, user_uuid):
        response = super_requests.get(
            url=self.endpoints.get_cart(user_uuid=user_uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = CartModel(**response.json())
        return model

    @allure.step("Add items to user's cart")
    def add_to_cart_item(self, user_uuid, game_uuid, quantity):
        response = super_requests.post(
            url=self.endpoints.add_item_user_cart(user_uuid=user_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.game_uuid(game_uuid=game_uuid, quantity=quantity)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = CartModel(**response.json())
        return model

    @allure.step("Change item in user's cart")
    def change_to_cart_item(self, user_uuid, game_uuid, quantity):
        response = super_requests.post(
            url=self.endpoints.change_item_user_cart(user_uuid=user_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.game_uuid(game_uuid=game_uuid, quantity=quantity)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = CartModel(**response.json())
        return model

    @allure.step("Clear user's cart")
    def clear_user_cart(self, user_uuid):
        response = super_requests.post(
            url=self.endpoints.clear_item_user_cart(user_uuid=user_uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = CartModel(**response.json())
        return model
