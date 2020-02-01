import json

from shobaserver import app


def test_perform():
    """Test the `/perform` path."""
    response = app.test_client().post(
        "/perform/simple",
        data=json.dumps({"colour": [0, 255, 0]}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json == {"status": "OK"}


def test_empty_post():
    """Test `/perform` handles an empty POST."""
    response = app.test_client().post(
        "/perform/simple", content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json == {"status": "OK"}


def test_bad_json():
    """Test `/perform` handles bad JSON."""
    response = app.test_client().post(
        "/perform/simple",
        data='{"colour": [0, 255, 0}',
        content_type="application/json",
    )
    assert response.status_code == 400


def test_matrix():
    """Test submitting a grid of colours to `/matrix`."""
    response = app.test_client().post(
        "/matrix",
        data=json.dumps({"matrix": [[[0, 255, 0]]]}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json == {"status": "OK"}


def test_no_matrix_data():
    """Test it handles no data."""
    response = app.test_client().post("/matrix", content_type="application/json",)
    assert response.status_code == 422
    assert response.json == {"error": "No data"}


def test_bad_matrix_data():
    """Test it handles bad data."""
    response = app.test_client().post(
        "/matrix",
        data=json.dumps({"poop": [[[255, 0, 255]]]}),
        content_type="application/json",
    )
    assert response.status_code == 422
    assert response.json == {"error": "Bad data"}
