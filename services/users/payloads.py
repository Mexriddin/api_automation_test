from faker import Faker

fake = Faker()


class Payloads:

    @classmethod
    def create_user(cls, field=None, value=None):
        data = {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name(),
            "nickname": fake.user_name()
        }
        if field is not None:
            if field == "email":
                data['email'] = value
            elif field == "nickname":
                data['nickname'] = value
        return data
