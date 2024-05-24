from faker import Faker
import random
import string
fake = Faker()



class Payloads:

    @classmethod
    def create_review(cls, user_uuid):
        return {
            "body": ''.join(random.choices(string.ascii_letters + string.digits, k=100)),
            "score": random.randint(1, 99999),
            "title": ''.join(random.choices(string.ascii_letters + string.digits, k=100)),
            "user_uuid": user_uuid
        }

    @classmethod
    def update_review(cls):
        return {
            "body": ''.join(random.choices(string.ascii_letters + string.digits, k=100)),
            "score": random.randint(1, 99999),
            "title": ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        }