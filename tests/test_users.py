import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title("Get all users")
    def test_get_all_users(self):
        users = self.api_users.get_all_users(0, 10)
        assert len(users.items)

    @pytest.mark.users
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user.uuid)

    @pytest.mark.users
    @allure.title("Update new user")
    def test_update_user(self):
        user = self.api_users.create_user()
        updated_user = self.api_users.update_user_by_id(user.uuid)
        assert updated_user.nickname != user.nickname

    @pytest.mark.users
    @allure.title("Delete new user")
    def test_delete_user(self):
        user = self.api_users.create_user()
        self.api_users.delete_user_by_id(user.uuid)
        self.api_users.get_user_by_id(user.uuid)
