from config.conf import HOST


class Endpoints:
    get_games_by_category = lambda self, category_uuid: f"{HOST}/categories/{category_uuid}/games"
    get_categories_list = f"{HOST}/categories"
