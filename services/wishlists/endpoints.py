from config.conf import HOST


class Endpoints:
    get_wishlists = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist"
    add_item_to_wishlists = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist/add"
    remove_item_to_wishlists = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist/remove"
