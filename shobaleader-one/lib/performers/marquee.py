from lib.conf import config
from lib.light_grid import LightGrid
from lib.performers.performer import Performer
from lib.text_banner import TextBanner
from lib.yeeter import yeet


class Marquee(Performer):
    """Scroll some text."""

    def __init__(self, **kwargs):
        """Construct."""
        super().__init__(**kwargs)
        self.defaults = {"colour": [255, 0, 0]}
        self.apply_defaults()
        self.config = config()
        self.banner = TextBanner(self.text)  # pylint:disable=E1101

    def perform(self):
        """Keep sending frames."""
        while True:  # nocov
            indeces = yeet(self.banner.width, self.config["panel"]["width"])
            for index, offset in indeces:
                pixels = self.banner.carve_slice(index)
                grid = LightGrid(pixels, offset)
                grid.map({1: self.colour})  # pylint:disable=E1101

                yield grid
