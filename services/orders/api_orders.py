from services.orders.endpoints import Endpoints
from config.headers import Headers
from services.orders.payloads import Payloads
from services.orders.params import Params
from services.orders.model.order_models import OrderModel, OrdersModel
from utils.super_requests import SuperRequests as super_requests
import allure


class OrderAPI:
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.payloads = Payloads()

    @allure.step("Get an order")
    def get_order(self, order_uuid):
        response = super_requests.get(
            url=self.endpoints.get_order(order_uuid=order_uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = OrderModel(**response.json())
        return model

    @allure.step("Delete an order")
    def delete_order(self, order_uuid):
        response = super_requests.delete(
            url=self.endpoints.delete_order(order_uuid=order_uuid),
            headers=self.headers.basic,
            params=self.params.keep_payments(False)
        )
        assert response.status_code == 204, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"

    @allure.step("List all orders for a user")
    def list_orders_for_user(self, user_uuid):
        response = super_requests.get(
            url=self.endpoints.list_orders_for_user(user_uuid=user_uuid),
            headers=self.headers.basic,
            params=self.params.list_params(offset=0, limit=10)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = OrdersModel(**response.json())
        return model

    @allure.step("Create a new order")
    def create_order(self, user_uuid, game_uuid, quantity):
        response = super_requests.post(
            url=self.endpoints.create_new_order(user_uuid=user_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.games(game_uuid=game_uuid, quantity=quantity)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = OrderModel(**response.json())
        return model

    @allure.step("Update an order status")
    def update_order_status(self, order_uuid):
        response = super_requests.patch(
            url=self.endpoints.update_order_status(order_uuid=order_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.status()
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = OrderModel(**response.json())
        return model

















