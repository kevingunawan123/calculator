import pytest

from app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Web Calculator" in response.data


@pytest.mark.parametrize(
    "a,b,op,expected",
    [
        ("2", "3", "add", "5.0"),
        ("10", "4", "subtract", "6.0"),
        ("7", "6", "multiply", "42.0"),
        ("9", "3", "divide", "3.0"),
    ],
)
def test_calculations(client, a, b, op, expected):
    response = client.post(
        "/",
        data={"a": a, "b": b, "op": op},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert expected.encode() in response.data


def test_divide_by_zero_shows_error(client):
    response = client.post("/", data={"a": "1", "b": "0", "op": "divide"})
    assert response.status_code == 200
    assert b"Cannot divide by zero." in response.data
