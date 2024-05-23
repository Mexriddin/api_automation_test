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
        assert len(games.games) >= 0

    @allure.title("Search game by name")
    def test_search_game_by_name(self):
        games = self.api_games.search_games_by_name("Atomic Heart")
        assert games.games[0].title == "Atomic Heart"

    @allure.title("Get a game")
    def test_get_game_by_uuid(self):
        games = self.api_games.get_list_all_games()
        game = self.api_games.get_game_by_uuid(games.games[0].uuid)
        assert game.uuid == games.games[0].uuid