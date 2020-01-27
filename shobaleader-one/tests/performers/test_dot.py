from lib.light_grid import LightGrid
from lib.performers.dot import Dot


class TestDot:
    """Test the Dot."""

    def test_constructor(self):
        """Test it gets the correct data."""

        data = {"colour": [255, 127, 0]}
        dot = Dot(**data)

        assert dot.colour == [255, 127, 0]

    def test_partial_constructor(self):
        """Test it fills in its defaults."""

        dot = Dot()

        assert dot.colour == [255, 0, 0]

    def test_frame(self):
        """Test it makes a frame."""

        dot = Dot()

        assert isinstance(dot.frame(), LightGrid)
