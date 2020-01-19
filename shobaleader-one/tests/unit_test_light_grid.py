from mock import patch

from lib.light_grid import LightGrid


class TestLightGrid:  # pylint: disable=W0613
    """Test the Grid."""

    @patch('lib.conf.config',
           return_value={'panel': {'width': 4, 'height': 2}})
    def test_constructor(self, config):
        """Test it configures itself correctly."""
        grid = LightGrid()

        assert grid.width == 4
        assert grid.height == 2

        assert grid == [
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    @patch('lib.conf.config',
           return_value={'panel': {'width': 4, 'height': 4}})
    def test_with_data(self, config):
        """Test it can take some initialisation data."""
        data = [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ]
        grid = LightGrid(data)

        assert grid == [
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0]
        ]

    @patch('lib.conf.config',
           return_value={'panel': {'width': 3, 'height': 3}})
    def test_with_offset_data(self, config):
        """Test it can take seed data at an abritrary (x, y)."""
        data = [
            [1],
            [1]
        ]
        grid = LightGrid(data, origin_x=2, origin_y=1)

        assert grid == [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 1]
        ]

    @patch('lib.conf.config',
           return_value={'panel': {'width': 4, 'height': 4}})
    def test_flattening(self, config):
        """Test it converts to a list correctly, folding left and right."""
        data = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 0]
        ]
        grid = LightGrid(data)
        assert grid.flattened == [
            1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0
        ]

    @patch('lib.conf.config',
           return_value={'panel': {'width': 4, 'height': 2}})
    def test_mapping(self, config):
        """Test it can populate itself with RGBs."""
        data = [
            [1, 2, 0, 1],
            [0, 0, 1, 1]
        ]
        grid = LightGrid(data)

        mappings = {
            1: [255, 0, 0],
            2: [0, 255, 0]
        }
        grid.map(mappings)

        assert grid == [
            [[255, 0, 0], [0, 255, 0], [0, 0, 0], [255, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0]],

        ]
