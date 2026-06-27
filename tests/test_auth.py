def test_register(client, test_user):
    response = client.post("/auth/register", json=test_user)

    assert response.status_code == 201

    data = response.json()

    assert "data" in data
    assert data["data"]["username"] == test_user["username"]
    assert data["data"]["email"] == test_user["email"]

def test_login(client, test_user):
    client.post("/auth/register", json=test_user)

    response = client.post(
        "/auth/login",
        data={
            "username": test_user["username"],
            "password": test_user["password"],
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    # Assert
    assert response.status_code == 200

    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_me_endpoint(client, test_user):
    # Arrange: register + login
    client.post("/auth/register", json=test_user)

    login_response = client.post(
        "/auth/login",
        data={
            "username": test_user["username"],
            "password": test_user["password"],
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    token = login_response.json()["access_token"]

    # Act
    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    # Assert
    assert response.status_code == 200

    data = response.json()
    assert data["username"] == test_user["username"]

def test_logout(client):
    response = client.post("/auth/logout")

    assert response.status_code == 200

    data = response.json()
    assert "message" in data