from lib.colour_tools import gamma_correct
from lib.conf import config
from lib.performers.simple import SimplePerformer


class TestSimple:
    """Test the SimplePerformer."""

    def test_iterator(self):
        """Test it implements an iterator."""
        simp = SimplePerformer()

        results = []

        for item in simp.perform():
            results.append(item)

        assert results[0] == [[[0, 0, 0]] * 32] * 8
        assert results[1] == [[gamma_correct(config()["colours"]["orange"])] * 32] * 8
