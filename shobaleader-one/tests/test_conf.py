from lib.conf import config


def test_config():
    """Test it reads the config correctly."""
    path = "tests/fixtures/config/config.yaml"
    assert config(path)["something"]["bar"] == ["apple", "banana", "carrot"]
