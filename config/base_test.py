from services.categories.api_categories import CategoryAPI
from services.commons.common_steps import CommonSteps
from services.users.api_users import UsersAPI
from services.wishlists.api_wishlists import WishlistAPI
from services.games.api_games import GameAPI
from services.carts.api_carts import CartAPI
from services.orders.api_orders import OrderAPI
from services.payments.api_payments import PaymentAPI


class BaseTest:
    def setup_method(self):
        self.common = CommonSteps()
        self.api_users = UsersAPI()
        self.api_wishlists = WishlistAPI()
        self.api_games = GameAPI()
        self.api_categories = CategoryAPI()
        self.api_carts = CartAPI()
        self.api_orders = OrderAPI()
        self.api_payments = PaymentAPI()