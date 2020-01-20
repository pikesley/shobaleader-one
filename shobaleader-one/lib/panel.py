from platform import platform

import lib.conf

ARM = False
if "arm" in platform():  # nocov
    ARM = True
    from neopixel import NeoPixel
    import board


class Panel:
    """Class representing the Longruner light panel."""

    def __init__(self):
        """Construct."""
        self.config = lib.conf.config()["panel"]
        self.width = self.config["width"]
        self.height = self.config["height"]
        self.length = self.width * self.height
        self.pixels = self.appropriate_pixels()

    def appropriate_pixels(self):
        """We can only have Real Pixels on an Actual Pi."""
        if ARM:
            return NeoPixel(board.D18, self.length, auto_write=False)  # nocov
        else:
            return FakePixel(self.length)

        # self.current_performer = None
        # self.current_args = None
        # self.process = None


class FakePixel(list):
    """Fake NeoPixels for testing."""

    def __init__(self, length):  # pylint: disable=W0231
        """Construct."""
        self.length = length
        for _ in range(self.length):
            self.append((0, 0, 0))
