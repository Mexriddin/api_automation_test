import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Categories")
@allure.feature("Everything about categories")
@pytest.mark.positive
@pytest.mark.categories
class TestCategories(BaseTest):

    @allure.title("List all categories")
    def test_get_all_categories(self):
        categories = self.api_categories.get_all_categories()
        assert len(categories.categories) >= 0

    @allure.title("Get games by category")
    def test_get_games_by_category(self):
        categories = self.api_categories.get_all_categories()
        games = self.api_categories.get_games_by_category(category_uuid=categories.categories[0].uuid)
        assert len(games.games) >= 0