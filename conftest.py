import requests
import pytest
from config.conf import HOST, API_TOKEN


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={"Authorization": f"Bearer {API_TOKEN}"}
    )
    assert response.status_code == 205


