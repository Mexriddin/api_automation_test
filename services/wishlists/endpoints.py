from config.conf import HOST


class Endpoints:
    get_wishlists = lambda self, uuid: f"{HOST}/users/{uuid}/wishlists"
    add_item_to_wishlists = lambda self, uuid: f"{HOST}/users/{uuid}/wishlists/add"
    remove_item_to_wishlists = lambda self, uuid: f"{HOST}/users/{uuid}/wishlists/remove"
