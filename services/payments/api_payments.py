from services.payments.endpoints import Endpoints
from config.headers import Headers
from services.payments.payloads import Payloads
from services.payments.params import Params
from services.payments.model.payment_models import PaymentModel, PaymentsModel
from utils.super_requests import SuperRequests as super_requests
import allure


class PaymentAPI:
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.payloads = Payloads()

    @allure.step("Get a payment")
    def get_payment(self, payment_uuid):
        response = super_requests.get(
            url=self.endpoints.get_payment(payment_uuid=payment_uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = PaymentModel(**response.json())
        return model

    @allure.step("Delete a payment")
    def delete_payment(self, payment_uuid):
        response = super_requests.delete(
            url=self.endpoints.delete_payment(payment_uuid=payment_uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 204, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"

    @allure.step("List all payments for user")
    def get_all_payments_for_user(self, user_uuid):
        response = super_requests.get(
            url=self.endpoints.list_orders_all_payments(user_uuid=user_uuid),
            headers=self.headers.basic,
            params=self.params.payment_list_params(offset=0, limit=10)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = PaymentsModel(**response.json())
        return model

    @allure.step("Create a new payment")
    def create_payment(self, user_uuid, order_uuid, payment_method):
        response = super_requests.post(
            url=self.endpoints.create_new_payment(user_uuid=user_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.payment(order_uuid=order_uuid, payment_method=payment_method)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = PaymentModel(**response.json())
        return model