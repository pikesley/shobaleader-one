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
