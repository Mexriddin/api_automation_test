import pytest
from services.users.api_users import UsersAPI
from services.games.api_games import GameAPI


@pytest.fixture(scope="function")
def user():
    user_api = UsersAPI()
    user = user_api.create_new_user()
    yield user


@pytest.fixture(scope="function")
def game():
    api_game = GameAPI()
    games = api_game.get_list_all_games()
    yield games.games[0]