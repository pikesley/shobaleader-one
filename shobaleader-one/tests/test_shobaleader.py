from mock import call, create_autospec

from lib.colour_tools import gamma_correct
from lib.conf import config
from lib.panel import Panel
from lib.performers.simple import SimplePerformer
from lib.shobaleader import Shobaleader


class TestShobaleader:
    """Test the Shobaleader."""

    def test_constructor(self):
        """Test it initialises correctly."""
        leader = Shobaleader()

        assert not leader.process
        assert not leader.performer_class

    def test_rendering(self):
        """Test it renders frames unto the Grid."""
        leader = Shobaleader()
        leader.panel = create_autospec(Panel)
        leader.performer_class = SimplePerformer
        leader.args = {}
        leader.render()
        assert leader.panel.display.mock_calls == [
            call([[[0, 0, 0]] * 32] * 8),
            call([[gamma_correct(config()["colours"]["orange"])] * 32] * 8),
        ]
