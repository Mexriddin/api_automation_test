from config.conf import HOST


class Endpoints:
    get_cart = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/cart"
    add_item_user_cart = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/cart/add"
    change_item_user_cart = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/cart/change"
    clear_item_user_cart = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/cart/clear"
    remove_item_user_cart = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/cart/remove"
