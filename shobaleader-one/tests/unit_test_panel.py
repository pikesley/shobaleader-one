from mock import patch

from lib.panel import FakePixel, Panel


@patch('lib.conf.config',
       return_value={'panel': {'width': 16, 'height': 4}})
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
