from faker import Faker

fake = Faker()


class Payloads:

    game_uuid = lambda self, uuid: {"item_uuid": uuid}