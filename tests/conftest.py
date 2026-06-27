import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)

import pytest
import uuid

@pytest.fixture
def test_user():
    unique_id = uuid.uuid4().hex[:8]

    return {
        "email": f"user_{unique_id}@example.com",
        "password": "Test1234"
    }