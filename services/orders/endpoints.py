from config.conf import HOST


class Endpoints:
    delete_order = lambda self, order_uuid: f"{HOST}/orders/{order_uuid}"
    get_order = lambda self, order_uuid: f"{HOST}/orders/{order_uuid}"
    update_order_status = lambda self, order_uuid: f"{HOST}/orders/{order_uuid}/status"
    list_orders_for_user = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/orders"
    create_new_order = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/orders"

