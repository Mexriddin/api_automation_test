import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Carts")
@allure.feature("Cart management")
@pytest.mark.positive
@pytest.mark.categories
class TestCart(BaseTest):

    @allure.title("Get new user cart")
    def test_get_cart(self):
        user = self.api_users.create_new_user()
        cart = self.api_carts.get_cart(user_uuid=user["model"].uuid)
        assert cart.user_uuid == user["model"].uuid
        assert cart.items.count() == 0

    @allure.title("Add default game to cart for new user")
    def test_add_item(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        cart = self.api_carts.add_to_cart_item(user_uuid=user["model"].uuid, game=games[0], quantity=1)
        assert cart.items[0].item_uuid == games[0].item_uuid
        assert cart.user_uuid == user["model"].uuid

    @allure.title("Change the quantity of games in the cart for a new user")
    def test_change_cart_item(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        cart = self.api_carts.add_to_cart_item(user_uuid=user["model"].uuid, game=games[0], quantity=5)
        changed_cart = self.api_carts.change_to_cart_item(user_uuid=cart.user_uuid, game_uuid=cart.items[0].item_uuid,
                                                          quantity=7)
        assert changed_cart.items[0].quantity == 5

    @allure.title("Clear cart, new user with items")
    def test_remove_cart_items(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        cart = self.api_carts.add_to_cart_item(user_uuid=user["model"].uuid, game=games[0], quantity=5)
        empty_cart = self.api_carts.clear_user_cart(user_uuid=cart.user_uuid)
        assert empty_cart.items.count() == 0
        assert empty_cart.total_quantity == 0

