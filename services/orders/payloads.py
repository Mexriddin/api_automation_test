from faker import Faker

fake = Faker()



class Payloads:

    @classmethod
    def games(cls, game_uuid, quantity=1):
        return {
            "items":
                {
                    "item_uuid": game_uuid,
                    "quantity": quantity
                }
        }

    @classmethod
    def status(cls):
        return {
            "status": "canceled"
        }