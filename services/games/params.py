from services.commons.params import BaseParams


class Params(BaseParams):
    search_games_params = lambda self, query: {"query": query}

