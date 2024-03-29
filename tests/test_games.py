import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Games")
@allure.feature("Everything about games")
@pytest.mark.positive
@pytest.mark.games
class TestGames(BaseTest):

    @allure.title("List all games")
    def test_get_all_games(self):
        games = self.api_games.get_list_all_games()
        assert len(games.items) >= 0

    @allure.title("Search game by name")
    def test_search_game_by_name(self):
        games = self.api_games.search_games_by_name("Atomic Heart")
        assert games.items[0].title == "Atomic Heart"

    @allure.title("Get a game")
    def test_get_game_by_uuid(self):
        user = self.api_users.create_new_user()
        game = self.api_games.get_game_by_uuid("1990ecdd-4d3d-4de2-91b9-d45d794c82bc")
        assert game.uuid == "1990ecdd-4d3d-4de2-91b9-d45d794c82bc"