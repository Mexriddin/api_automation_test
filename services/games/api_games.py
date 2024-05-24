from services.games.payloads import Payloads
from services.games.endpoints import Endpoints
from config.headers import Headers
from services.games.params import Params
from services.games.models.game_models import GameModel, GamesModel
from utils.super_requests import SuperRequests as super_requests
import allure


class GameAPI:
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()

    @allure.step("List all games")
    def get_list_all_games(self, offset=0, limit=10):
        response = super_requests.get(
            url=self.endpoints.get_all_games,
            headers=self.headers.basic,
            params=self.params.list_params(offset=offset, limit=limit)
        )
        assert response.status_code == 200, response.json()
        model = GamesModel(**response.json())
        return model

    @allure.step("Search games")
    def search_games_by_name(self, name, offset=0, limit=10):
        response = super_requests.get(
            url=self.endpoints.get_search_games,
            headers=self.headers.basic,
            params={
                **self.params.search_games_params(query=name),
                **self.params.list_params(offset=offset, limit=limit)
            }
        )
        assert response.status_code == 200, response.json()
        model = GamesModel(**response.json())
        return model

    @allure.step("Get a game")
    def get_game_by_uuid(self, uuid):
        response = super_requests.get(
            url=self.endpoints.get_game_by_uuid(uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        model = GameModel(**response.json())
        return model



