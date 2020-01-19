from mock import patch

from lib.panel import Panel


class TestPanel:
    """Test the Panel."""

    @patch('lib.conf.config',
           return_value={'panel': {'width': 16, 'height': 4}})
    def test_constructor(self, config):  # pylint: disable=W0613
        """Test it configures itself correctly."""
        panel = Panel()

        assert panel.width == 16
        assert panel.height == 4
        assert panel.length == 64
