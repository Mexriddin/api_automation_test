from faker import Faker

fake = Faker()



class Payloads:

    @classmethod
    def payment(cls, order_uuid, payment_method):
        return {
            "order_uuid": order_uuid,
            "payment_method": payment_method
        }