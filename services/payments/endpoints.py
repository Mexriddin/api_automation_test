from config.conf import HOST


class Endpoints:
    delete_payment = lambda self, payment_uuid: f"{HOST}/payments/{payment_uuid}"
    get_payment = lambda self, payment_uuid: f"{HOST}/payments/{payment_uuid}"
    list_all_payments_for_order = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/payments"
    create_new_payment = lambda self, user_uuid: f"{HOST}/users/{user_uuid}/payments"

