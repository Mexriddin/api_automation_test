from services.reviews.endpoints import Endpoints
from config.headers import Headers
from services.reviews.payloads import Payloads
from services.reviews.params import Params
from services.reviews.model.review_models import ReviewModel, ReviewsModel
from utils.super_requests import SuperRequests as super_requests
import allure


class ReviewAPI:
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.payloads = Payloads()

    @allure.step("Update a review")
    def update_review(self, review_uuid):
        response = super_requests.patch(
            url=self.endpoints.update_review(review_uuid=review_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.update_review()
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = ReviewModel(**response.json())
        return model

    @allure.step("Delete a review")
    def delete_payment(self, review_uuid):
        response = super_requests.delete(
            url=self.endpoints.delete_review(review_uuid=review_uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 204, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"

    @allure.step("List all reviews for games")
    def get_all_reviews_for_game(self, game_uuid):
        response = super_requests.get(
            url=self.endpoints.list_all_reviews_for_game(game_uuid=game_uuid),
            headers=self.headers.basic,
            params=self.params.reviews_list_params(offset=0, limit=10, sort="created_at", order_by="asc")
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = ReviewsModel(**response.json())
        return model

    @allure.step("Create a new review")
    def create_review(self, game_uuid, user_uuid):
        response = super_requests.post(
            url=self.endpoints.create_new_review(game_uuid=game_uuid),
            headers=self.headers.basic,
            json_data=self.payloads.create_review(user_uuid=user_uuid)
        )
        assert response.status_code == 200, f"Actual status_code:{response.status_code}\nResponse:{response.json()}"
        model = ReviewModel(**response.json())
        return model