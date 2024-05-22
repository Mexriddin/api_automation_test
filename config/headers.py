from config.conf import API_TOKEN


class Headers:

    basic = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json",
        "X-Task-Id": "API-2"
    }