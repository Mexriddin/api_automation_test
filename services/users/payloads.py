from faker import Faker

fake = Faker()



class Payloads:

    @classmethod
    def create_new_user(cls):
        return {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name(),
            "nickname": fake.user_name()
    }

    @classmethod
    def create_exist_user(cls, field=None, value=None):
        data = cls.create_new_user()
        if field is not None:
            if field == "email":
                data['email'] = value
            elif field == "nickname":
                data['nickname'] = value
        return data


    @classmethod
    def login_without_field(cls, login_data, field=None):
        data = {}
        if field is not None:
            if field == "email":
                data['email'] = ""
                data['password'] = login_data["password"]
            elif field == "password":
                data['email'] = login_data["email"]
                data['password'] = ""
        return data

    @classmethod
    def users_avatar(cls):
        files = {
            "avatar_file": open("avatar.jpeg", "rb")
        }
        return files