import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_request_factory():
    return APIRequestFactory()


@pytest.fixture(autouse=True)
def disable_network_access(monkeypatch):
    """Prevent any un-mocked network requests from executing in tests"""

    def fail(*args, **kwargs):
        pytest.fail('Called network method in test')

    monkeypatch.setattr('socket.socket', fail)
