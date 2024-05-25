import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Orders")
@allure.feature("Orders management")
@pytest.mark.positive
@pytest.mark.orders
@pytest.mark.skip("Does not have premium permissions")
class TestOrder(BaseTest):
    @allure.title("Created order for new user")
    def test_create_order(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_id=games.games[0].uuid)
        assert order.status == "open"
        assert order.items[0].item_uuid == games.games[0].uuid
        assert order.user_uuid == user["model"].uuid

    @allure.title("Get an order")
    def test_get_order(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        new_order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_id=games.games[0].uuid)
        order = self.api_orders.get_order(order_id=new_order.uuid)
        assert order.uuid == new_order.uuid
        assert order.user_uuid == user["model"].uuid

    @allure.title("List all orders for new user")
    def test_list_orders(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        firs_order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_uuid=games.games[0].uuid, quantity=4)
        second_order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_uuid=games.games[1].uuid, quantity=4)
        orders = self.api_orders.list_orders_for_user(user_uuid=user["model"].uuid)
        assert orders.orders[1].uuid == firs_order.uuid
        assert orders.orders[0].uuid == second_order.uuid
        assert orders.orders[0].user_uuid == user["model"].uuid
        assert orders.orders[1].user_uuid == user["model"].uuid

    @allure.title("Update an order status for new user")
    def test_update_order_status(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_uuid=games.games[0].uuid)
        self.api_orders.update_order_status(order_uuid=order.uuid)
        updated_order = self.api_orders.get_order(order_uuid=order.uuid)
        assert updated_order.status == "canceled"

    @allure.title("Delete an order status for new user")
    def test_delete_order(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_uuid=games.games[0].uuid)
        self.api_orders.delete_order(order_uuid=order.uuid)
