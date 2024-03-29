from config.conf import HOST


class Endpoints:
    get_all_games = f"{HOST}/games"
    get_search_games = f"{HOST}/games"
    get_game_by_uuid = lambda self, uuid: f"{HOST}/games/{uuid}"
