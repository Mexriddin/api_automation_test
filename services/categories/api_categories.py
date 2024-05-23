from services.categories.endpoints import Endpoints
from config.headers import Headers
from services.categories.params import Params
from services.categories.models.category_models import CategoryModel, CategoriesModel
from services.games.models.game_models import GamesModel
from utils.super_requests import SuperRequests as super_requests
import allure


class CategoryAPI:
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()

    @allure.step("Get all categories")
    def get_all_categories(self, offset=0, limit=10):
        response = super_requests.get(
            url=self.endpoints.get_categories_list,
            headers=self.headers.basic,
            params=self.params.categories_list_params(offset=offset, limit=limit)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = CategoriesModel(**response.json())
        return model

    @allure.step("Get games by category")
    def get_games_by_category(self, category_uuid, offset=0, limit=10):
        response = super_requests.get(
            url=self.endpoints.get_games_by_category(category_uuid=category_uuid),
            headers=self.headers.basic,
            params=self.params.categories_list_params(offset=offset, limit=limit)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = GamesModel(**response.json())
        return model