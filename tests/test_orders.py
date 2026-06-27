import pytest


def get_token(client, test_user):
    client.post("/auth/register", json=test_user)

    login_response = client.post(
        "/auth/login",
        data={
            "username": test_user["email"],
            "password": test_user["password"],
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    return login_response.json()["access_token"]


def test_create_order(client, test_user):
    token = get_token(client, test_user)

    # IMPORTANT: we assume product with id=1 exists in test DB
    payload = {
        "product_id": 1
    }

    response = client.post(
        "/orders",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 201 or 200

    data = response.json()

    assert "data" in data
    assert data["data"]["product_id"] == 1


def test_order_receipt(client, test_user):
    token = get_token(client, test_user)

    # Step 1: create order
    create_response = client.post(
        "/orders",
        json={"product_id": 1},
        headers={"Authorization": f"Bearer {token}"}
    )

    order_id = create_response.json()["data"]["id"]

    # Step 2: fetch order receipt
    response = client.get(
        f"/orders/{order_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert data["data"]["id"] == order_id