import lib.conf


class LightGrid(list):
    """Abstraction for the actual NeoPixels on the Panel."""

    # pylint: disable=W0231,W0102
    def __init__(self, data=[[]], origin_x=0, origin_y=0):
        """Construct."""
        self.config = lib.conf.config()["panel"]
        self.width = self.config["width"]
        self.height = self.config["height"]
        self.origin_x = origin_x
        self.origin_y = origin_y

        for _ in range(self.height):
            self.append([0] * self.width)

        self.seed(data)

    def seed(self, data):
        """Insert the seed data."""
        for index, _ in enumerate(data):
            row_index = index + self.origin_y
            self[row_index][self.origin_x : len(data[index])] = data[index]
            del self[row_index][self.width :]

    @property
    def flattened(self):
        """Convert to a list, with rows reversed appropriately."""
        flat = []

        for index, row in enumerate(self):
            if index % 2 == 1:
                row = reversed(row)

            flat.extend(row)

        return flat

    def map(self, mappings={}):
        """Populate ourself with useful data."""
        for i, _ in enumerate(self):
            for j, _ in enumerate(self[i]):
                try:
                    self[i][j] = mappings[self[i][j]]
                except KeyError:
                    self[i][j] = [0, 0, 0]
