import pytest
from fastapi.testclient import TestClient

from src.aula01.app import app


@pytest.fixture
def client():
    return TestClient(app)
