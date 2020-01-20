from mock import MagicMock
from lib.shobaleader import Shobaleader


class TestShobaleader:
    """Test the Shobaleader."""

    def test_constructor(self):
        """Test it initialises correctly."""
        panel = MagicMock()
        leader = Shobaleader(panel)

        assert not leader.process
        assert not leader.performer
