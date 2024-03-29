import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Users")
@pytest.mark.positive
@pytest.mark.users
class TestUsers(BaseTest):

    @allure.title("List all users with default params")
    def test_get_all_users_with_default_params(self):
        users = self.api_users.get_all_users()
        assert len(users.items) == 10

    @allure.title("Get all users with manual params")
    def test_get_all_users_with_params(self):
        users = self.api_users.get_all_users(0, 5)
        assert len(users.items) == 5

    @allure.title("Create a new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user["model"].uuid)

    @allure.title("Login a new user")
    def test_login_user(self):
        user = self.api_users.create_user()
        login_user = self.api_users.login_user(user["login_data"]["email"], user["login_data"]["password"])
        assert user["model"] == login_user

    @allure.title("Update new user")
    def test_update_user(self):
        user = self.api_users.create_user()
        updated_user = self.api_users.update_user_by_id(user["model"].uuid)
        assert updated_user.nickname != user["model"].nickname

    @allure.title("Delete new user")
    def test_delete_user(self):
        user = self.api_users.create_user()
        self.api_users.delete_user_by_id(user["model"].uuid)
