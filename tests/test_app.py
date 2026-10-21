
import pytest
from app import app


@pytest.fixture
def client(tmp_path):
    database = tmp_path / "test.db"
    app.config["DATABASE"] = str(database)

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"My To-Do List" in response.data


def test_add_task(client):
    response = client.post(
        "/add",
        data={"title": "Finish DevOps project"},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Finish DevOps project" in response.data


def test_empty_task_not_added(client):
    response = client.post(
        "/add",
        data={"title": "   "},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"No tasks yet" in response.data


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_metrics_endpoint(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"todo_http_requests_total" in response.data
