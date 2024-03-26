from config.conf import HOST


class Endpoints:

    create_user = f"{HOST}/users"
    login_user = f"{HOST}/users/login"
    get_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    update_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    delete_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    get_users_list = f"{HOST}/users"
