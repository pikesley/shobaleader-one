import pickle

from lib.conf import config


class TextBanner:
    """Text on a grid."""

    def __init__(self, text, font="spectrum/slim"):
        """Construct."""
        self.text = text
        self.font = pickle.load(open(f"fonts/{font}.pickle", "rb"))
        self.chars = list(self.text)
        self.grid = self.make_grid()
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def make_grid(self):
        """Turn the text into a grid."""
        grid = []
        for index, _ in enumerate(self.font[self.chars[0]]):
            grid.append([])

        for char in self.chars:
            for index in range(config()["panel"]["height"]):
                grid[index].extend(self.font[char][index])

        return grid

    def carve_slice(
        self, x_index=0, width=config()["panel"]["width"],
    ):
        """Carve out a piece of our grid."""
        piece = []
        for row in self.grid:
            piece.append(row[x_index : x_index + width])

        return piece
