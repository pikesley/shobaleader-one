from time import sleep

from lib.conf import config
from lib.light_grid import LightGrid
from lib.performers.performer import Performer
from lib.text_banner import TextBanner
from lib.yeeter import yeeter


class Marquee(Performer):
    """Scroll some text."""

    def __init__(self, **kwargs):
        """Construct."""
        super().__init__(**kwargs)
        self.defaults = {"colour": [255, 0, 0], "delay": 0.01}
        self.apply_defaults()
        self.config = config()
        self.banner = TextBanner(self.text)

    def perform(self):
        """Keep sending frames."""
        while True:  # nocov
            for index, offset in yeeter(
                self.banner.width, self.config["panel"]["width"]
            ):
                pixels = self.banner.carve_slice(index)
                grid = LightGrid(pixels, offset)
                grid.map({1: self.colour})

                yield grid
                sleep(self.delay)
