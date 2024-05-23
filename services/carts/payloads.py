import random
from faker import Faker

fake = Faker()



class Payloads:

    @classmethod
    def game_uuid(cls, game_uuid, quantity=1):
        return {
            "item_uuid": game_uuid,
            "quantity": quantity
    }
