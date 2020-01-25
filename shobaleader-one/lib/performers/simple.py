from lib.light_grid import LightGrid


class SimplePerformer:
    """Very simple performer, for testing."""

    def perform(self, colour=None):
        """Keep sending frames."""
        if not colour:
            colour = [255, 0, 0]

        data = [[1] * 32] * 8
        for number in [0, 1]:
            data = [[number] * 32] * 8
            grid = LightGrid(data)
            grid.map({1: colour})
            yield grid
