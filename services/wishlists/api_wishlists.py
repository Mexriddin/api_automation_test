from services.wishlists.payloads import Payloads
from services.wishlists.endpoints import Endpoints
from config.headers import Headers
from services.wishlists.models.wishlist_model import WishlistsModel
from utils.super_requests import SuperRequests as super_requests
import allure


class WishlistAPI:
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Get wishlists by user UUID")
    def get_wishlists_by_uuid(self, uuid):
        response = super_requests.get(
            url=self.endpoints.get_wishlists(uuid=uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        model = WishlistsModel(**response.json())
        return model

    @allure.step("Add game to user wishlist")
    def add_item_to_user_wishlist(self, user_uuid, game_uuid):
        response = super_requests.post(
            url=self.endpoints.add_item_to_wishlists(user_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.game_uuid(game_uuid)
        )
        assert response.status_code == 200, response.json()

    @allure.step("Remove game from user wishlist")
    def remove_item_from_user_wishlist(self, user_uuid, game_uuid):
        response = super_requests.post(
            url=self.endpoints.remove_item_to_wishlists(user_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.game_uuid(game_uuid)
        )
        assert response.status_code == 200, response.json()