
class Params:
    game_list_params = lambda self, offset, limit: {"offset": offset, "limit": limit}
    search_games_params = lambda self, query, offset, limit: {"query": query, "offset": offset, "limit": limit}
