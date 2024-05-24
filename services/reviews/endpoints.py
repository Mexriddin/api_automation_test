from config.conf import HOST


class Endpoints:
    list_all_reviews_for_game = lambda self, game_uuid: f"{HOST}/games/{game_uuid}/reviews"
    create_new_review = lambda self, game_uuid: f"{HOST}/games/{game_uuid}/reviews"
    delete_review = lambda self, review_uuid: f"{HOST}/reviews/{review_uuid}"
    update_review = lambda self, review_uuid: f"{HOST}/reviews/{review_uuid}"

