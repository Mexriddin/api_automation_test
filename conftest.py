import requests
import pytest
from config.conf import HOST, API_TOKEN


@pytest.fixture(autouse=True, scope="class")
def init_environment():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={"Authorization": f"Bearer {API_TOKEN}",
                 "X-Task-Id": "API-2"}
    )
    assert response.status_code == 205


