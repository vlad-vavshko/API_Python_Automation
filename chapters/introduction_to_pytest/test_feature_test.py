import pytest
import requests


@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():
    # Arrange
    url = 'https://duckduckgo.com/ac/?q=python+programing'

    # Act
    response = requests.get(url=url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert len(body) > 0
