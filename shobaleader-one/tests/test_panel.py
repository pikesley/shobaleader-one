from mock import patch

from lib.light_grid import LightGrid
from lib.panel import FakePixel, Panel


@patch("lib.conf.config", return_value={"panel": {"width": 16, "height": 4}})
class TestPanel:  # pylint: disable=W0613
    """Test the Panel."""

    def test_constructor(self, config):
        """Test it configures itself correctly."""
        panel = Panel()

        assert panel.width == 16
        assert panel.height == 4
        assert panel.length == 64

    def test_correct_pixels(self, config):
        """Test it gets FakePixels in test."""
        panel = Panel()

        assert isinstance(panel.pixels, FakePixel)

    def test_display(self, config):
        """Test the colours make it to the panel."""
        panel = Panel()
        data = [[1, 2], [3, 4]]
        grid = LightGrid(data, origin_x=7, origin_y=1)
        grid.map({1: [255, 0, 0], 2: [0, 255, 0], 3: [0, 0, 255], 4: [255, 255, 255]})
        panel.display(grid)
        assert panel.pixels == [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 255, 0],
            [255, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 255],
            [255, 255, 255],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
