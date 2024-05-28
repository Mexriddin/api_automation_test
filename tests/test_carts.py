import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Carts")
@allure.feature("Cart management")
@pytest.mark.positive
@pytest.mark.carts
@pytest.mark.skip("Does not have premium permissions")
class TestCart(BaseTest):

    @allure.title("Get user cart")
    def test_get_cart(self, user):
        cart = self.api_carts.get_cart(user_uuid=user["model"].uuid)
        assert cart.user_uuid == user["model"].uuid
        assert cart.items.count() == 0

    @allure.title("Add default game to cart for user")
    def test_add_item(self, user, game):
        cart = self.api_carts.add_to_cart_item(user_uuid=user["model"].uuid, game_uuid=game.uuid, quantity=1)
        assert cart.items[0].item_uuid == game.uuid
        assert cart.user_uuid == user["model"].uuid

    @allure.title("Change the quantity of games in the cart for a user")
    def test_change_cart_item(self, user, game):
        cart = self.api_carts.add_to_cart_item(user_uuid=user["model"].uuid, game_uuid=game.uuid, quantity=5)
        changed_cart = self.api_carts.change_to_cart_item(user_uuid=cart.user_uuid, game_uuid=cart.items[0].item_uuid,
                                                          quantity=7)
        assert changed_cart.items[0].quantity == 5

    @allure.title("Clear cart, user with items")
    def test_remove_cart_items(self, user, game):
        cart = self.api_carts.add_to_cart_item(user_uuid=user["model"].uuid, game_uuid=game.uuid, quantity=5)
        empty_cart = self.api_carts.clear_user_cart(user_uuid=cart.user_uuid)
        assert empty_cart.items.count() == 0
        assert empty_cart.total_quantity == 0
