import pytest


def get_token(client, test_user):
    # register
    client.post("/auth/register", json=test_user)

    # login
    login_response = client.post(
        "/auth/login",
        data={
            "username": test_user["email"],
            "password": test_user["password"],
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    return login_response.json()["access_token"]


def test_list_products(client, test_user):
    token = get_token(client, test_user)

    response = client.get(
        "/products",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert isinstance(data["data"], list)


def test_list_products_with_query_params(client, test_user):
    token = get_token(client, test_user)

    response = client.get(
        "/products?skip=0&limit=5",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    data = response.json()
    assert "data" in data


def test_product_details(client, test_user):
    token = get_token(client, test_user)

    list_response = client.get(
        "/products",
        headers={"Authorization": f"Bearer {token}"}
    )

    products = list_response.json()["data"]

    assert len(products) > 0

    product_id = products[0]["id"]

    response = client.get(
        f"/products/{product_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert data["data"]["id"] == product_id