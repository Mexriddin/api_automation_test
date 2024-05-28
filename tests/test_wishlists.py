import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Wishlist")
@allure.feature("Everything about users wishlists")
@pytest.mark.positive
@pytest.mark.wishlist
class TestWishlists(BaseTest):

    @allure.title("Get all wishlist new user")
    def test_get_all_wishlists_new_user(self, user):
        wishlists = self.api_wishlists.get_wishlists_by_uuid(user['model'].uuid)
        assert len(wishlists.items) == 0

    @allure.title("Add item to users wishlist")
    def test_add_item_to_user_wishlist(self, user, game):
        self.api_wishlists.add_item_to_user_wishlist(user_uuid=user['model'].uuid, game_uuid=game.uuid)
        wishlists = self.api_wishlists.get_wishlists_by_uuid(user['model'].uuid)
        assert len(wishlists.items) > 0


    @allure.title("Remove item from users wishlist")
    def test_remove_item_from_user_wishlist(self, user, game):
        self.api_wishlists.add_item_to_user_wishlist(user_uuid=user['model'].uuid, game_uuid=game.uuid)
        wishlists = self.api_wishlists.get_wishlists_by_uuid(user['model'].uuid)
        self.api_wishlists.remove_item_from_user_wishlist(user_uuid=wishlists.user_uuid, game_uuid=wishlists.items[0].uuid)
        wishlists = self.api_wishlists.get_wishlists_by_uuid(user['model'].uuid)
        assert len(wishlists.items) == 0
