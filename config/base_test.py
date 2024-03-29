from services.users.api_users import UsersAPI
from services.wishlists.api_wishlists import WishlistAPI
from services.games.api_games import GameAPI


class BaseTest:
    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_wishlists = WishlistAPI()
        self.api_games = GameAPI()