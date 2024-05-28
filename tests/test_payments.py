import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Payment")
@allure.feature("Payment management")
@pytest.mark.positive
@pytest.mark.categories
@pytest.mark.skip("Does not have premium permissions")
class TestPayment(BaseTest):
    @allure.title("Created a new payment")
    def test_create_payment(self, user, game):
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_id=game.uuid)
        payment = self.api_payments.create_payment(user_uuid=user["model"].uuid, order_uuid=order.uuid,
                                                   payment_method="card")
        assert payment.status == "succeeded"
        assert payment.order_uuid == order.uuid
        assert payment.user_uuid == user["model"].uuid

    @allure.title("Get a payment")
    def test_get_payment(self, user, game):
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_id=game.uuid)
        new_payment = self.api_payments.create_payment(user_uuid=user["model"].uuid, order_uuid=order.uuid,
                                                       payment_method="mir_pay")
        payment = self.api_payments.get_payment(user_uuid=user["model"].uuid, payment_uuid=new_payment.uuid)
        assert payment.user_uuid == user["model"].uuid
        assert payment.uuid == new_payment.uuid
        assert payment.order_uuid == order.uuid

    @allure.title("List all payments for new user")
    def test_list_payments(self, user, game):
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_id=game.uuid)
        payment = self.api_payments.create_payment(user_uuid=user["model"].uuid, order_uuid=order.uuid,
                                                   payment_method="paypal")
        payments = self.api_payments.get_all_payments_for_user(user_uuid=user["model"].uuid)
        assert payments.payments[0].user_uuid == user["model"].uuid
        assert payments.payments[0].order_uuid == order.uuid
        assert payments.payments[0].uuid == payment.uuid


    @allure.title("Delete a payment for new user")
    def test_delete_payment(self, user, game):
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_id=game.uuid)
        payment = self.api_payments.create_payment(user_uuid=user["model"].uuid, order_uuid=order.uuid,
                                                   payment_method="paypal")
        self.api_payments.delete_payment(payment_uuid=payment.uuid)
