import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Users")
@allure.suite("Positive")
@pytest.mark.positive
@pytest.mark.users
class TestUsersPositive(BaseTest):

    @allure.title("List all users with default params")
    def test_get_all_users_with_default_params(self):
        users = self.api_users.get_all_users()
        assert len(users.users) == 10

    @allure.title("Get all users with manual params")
    def test_get_all_users_with_params(self):
        users = self.api_users.get_all_users(0, 5)
        assert len(users.users) == 5

    @allure.title("Create a new user")
    def test_create_user(self):
        user = self.api_users.create_new_user()
        self.api_users.get_user_by_id(user["model"].uuid)

    @allure.title("Login a new user")
    def test_login_user(self):
        user = self.api_users.create_new_user()
        login_user = self.api_users.login_user(user["login_data"]["email"], user["login_data"]["password"])
        assert user["model"] == login_user

    @allure.title("Update new user")
    def test_update_user(self):
        user = self.api_users.create_new_user()
        updated_user = self.api_users.update_user_by_id(user["model"].uuid)
        assert updated_user.nickname != user["model"].nickname

    @allure.title("Delete new user")
    def test_delete_user(self):
        user = self.api_users.create_new_user()
        self.api_users.delete_user_by_id(user["model"].uuid)

    @allure.title("Update users avatar")
    @pytest.mark.skip("Does not have premium permissions")
    def test_update_avatar(self):
        user = self.api_users.create_new_user()
        user = self.api_users.update_user_avatar(user["model"].uuid)

@allure.epic("Administration")
@allure.feature("Users")
@allure.suite("Negative")
@pytest.mark.negative
@pytest.mark.users
class TestUsersNegative(BaseTest):
    @allure.title("Get list user without authentication")
    def test_get_list_user_without_token(self):
        error = self.api_users.get_all_users_without_token()
        self.common.assert_error_msg(error, 401, "security requirements failed: authentication failed")

    @allure.title("Get user with {invalid} uuid")
    @pytest.mark.parametrize("invalid_uuid, invalid", [("cb8e4476-e987-4990-b2a6-a2584b0079d", "minimum"),
                                                       ("cb8e4476-e987-4990-b2a6-a2584b0079d95", "maximum")])
    def test_get_user_with_invalid_uuid(self, invalid_uuid, invalid):
        error = self.api_users.get_user_by_invalid_uuid(invalid_uuid)
        self.common.assert_error_msg(error, 400, f'parameter \"user_uuid\" in path has an error: '
                                                 f'{invalid} string length is 36')

    @allure.title("Get not exist user")
    def test_get_not_exist_user(self):
        user = self.api_users.create_new_user()["model"]
        self.api_users.delete_user_by_id(user.uuid)
        error = self.api_users.get_not_exist_user(user.uuid)
        self.common.assert_error_msg(error, 404, f'Could not find user with "uuid": {user.uuid}')


    @allure.title("Create user with exist {field}")
    @pytest.mark.parametrize("field", ["email", "nickname"])
    def test_create_exist_user(self, field):
        user = self.api_users.create_new_user()
        error = self.api_users.create_user_exist(field, user["login_data"][field])
        self.common.assert_error_msg(error, 409, f'User with the following "{field}" already exists: {user['login_data'][field]}')

    @allure.title("Login without field: {field}")
    @pytest.mark.parametrize("field", ["email", "password"])
    def test_login_with_invalid_field(self, field):
        user = self.api_users.create_new_user()
        error = self.api_users.login_user_without_filed(user["login_data"], field)
        self.common.assert_error_msg(error, 400, f"Error at \"/{field}\"")

    @allure.title("Delete not exist user")
    def test_delete_not_exist_user(self):
        user = self.api_users.create_new_user()
        self.api_users.delete_user_by_id(user['model'].uuid)
        error = self.api_users.delete_not_exist_user(user['model'].uuid)
        self.common.assert_error_msg(error, 404, f'Could not find user with "uuid": {user["model"].uuid}')
