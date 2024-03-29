from faker import Faker

fake = Faker()


class Payloads:

    item_uuid = lambda self, uuid: {"item_uuid": uuid}