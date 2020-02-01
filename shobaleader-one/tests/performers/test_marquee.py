from lib.light_grid import LightGrid
from lib.performers.marquee import Marquee


class TestMarquee:
    """Test the Marquee."""

    def test_constructor(self):
        """Test it gets the correct data."""

        data = {"colour": [255, 127, 0], "text": "It is a period of civil war"}
        marquee = Marquee(**data)

        assert marquee.colour == [255, 127, 0]
        assert marquee.text == "It is a period of civil war"
