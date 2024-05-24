import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Review")
@allure.feature("Reviews management")
@pytest.mark.positive
@pytest.mark.reviews
class TestReview(BaseTest):
    @allure.title("Created a new review")
    def test_create_review(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        review = self.api_reviews.create_review(game_uuid=games.games[0].uuid, user_id=user["model"].uuid)
        assert review.user_uuid == user["model"].uuid

    @allure.title("List all reviews for a game")
    def test_list_reviews(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        order = self.api_orders.create_order(user_uuid=user["model"].uuid, game_id=games.games[0].uuid)
        review = self.api_reviews.create_review(game_uuid=games.games[0].uuid, user_id=user["model"].uuid)
        reviews = self.api_reviews.get_all_reviews_for_game(game_uuid=games.games[0].uuid)
        assert reviews.reviews[0].user_uuid == review.uuid
        assert reviews.reviews[0].order_uuid == order.uuid
        assert reviews.reviews[0].uuid == review.uuid


    @allure.title("Delete a review")
    def test_delete_review(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        review = self.api_reviews.create_review(game_uuid=games.games[0].uuid, user_id=user["model"].uuid)
        self.api_reviews.delete_payment(review_uuid=review.uuid)

    @allure.title("Update a review")
    def test_update_review(self):
        user = self.api_users.create_new_user()
        games = self.api_games.get_list_all_games()
        review = self.api_reviews.create_review(game_uuid=games.games[0].uuid, user_id=user["model"].uuid)
        updated_review = self.api_reviews.update_review(review_uuid=review.uuid)
        assert updated_review.user_uuid == user["model"].uuid
        assert updated_review.uuid == review.uuid
