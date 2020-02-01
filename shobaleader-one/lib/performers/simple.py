from lib.conf import config
from lib.light_grid import LightGrid
from lib.performers.performer import Performer


class SimplePerformer(Performer):
    """Very simple performer, for testing."""

    def __init__(self, **kwargs):
        """Construct."""
        super().__init__(**kwargs)
        self.apply_defaults()

    def perform(self):
        """Just send two frames (this is really just for testing)."""

        data = [[1] * config()["panel"]["width"]] * config()["panel"]["height"]
        for number in [0, 1]:
            data = [[number] * config()["panel"]["width"]] * config()["panel"]["height"]
            grid = LightGrid(data)
            grid.map({1: self.colour})
            yield grid
