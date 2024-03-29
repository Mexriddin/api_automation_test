import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Wishlist")
@allure.feature("Everything about users wishlists")
@pytest.mark.positive
@pytest.mark.wishlist
class TestWishlists(BaseTest):

    @allure.title("Get user's all wishlists")
    def test_get_all_wishlists_new_user(self):
        user = self.api_users.create_new_user()
        wishlists = self.api_wishlists.get_wishlists_by_uuid("1990ecdd-4d3d-4de2-91b9-d45d794c82bc")
        assert len(wishlists.items) != 0

