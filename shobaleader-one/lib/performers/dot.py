from random import randint

from lib.conf import config
from lib.light_grid import LightGrid


class Dot:
    """Just a dot, leaping around."""

    def perform(self, colour=None):
        """Keep sending frames."""
        if not colour:
            colour = [255, 0, 0]

        while True:
            x = randint(0, config()["panel"]["width"] - 1)
            y = randint(0, config()["panel"]["height"] - 1)
            data = [[1]]
            grid = LightGrid(data, origin_x=x, origin_y=y)
            grid.map({1: colour})
            yield grid
