from random import randint

from lib.colour_tools import complementary
from lib.conf import config
from lib.light_grid import LightGrid
from lib.performers.performer import Performer


class Dot(Performer):
    """Just a dot, leaping around."""

    def __init__(self, **kwargs):
        """Construct."""
        super().__init__(**kwargs)
        self.defaults = {"colour": [255, 0, 0]}
        self.apply_defaults()

    def frame(self):
        """Make one frame."""
        x = randint(0, config()["panel"]["width"] - 3)
        y = randint(0, config()["panel"]["height"] - 3)
        data = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
        grid = LightGrid(data, origin_x=x, origin_y=y)
        grid.map(
            {1: self.colour, 2: complementary(self.colour)}  # pylint:disable=E1101
        )

        return grid

    def perform(self):
        """Keep sending frames."""

        while True:  # nocov
            yield self.frame()
