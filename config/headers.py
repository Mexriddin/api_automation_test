from config.conf import API_TOKEN


class Headers:

    basic = {
        "Authorization": f"Bearer {API_TOKEN}"
    }