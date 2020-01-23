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
        assert results[1] == [[[255, 0, 0]] * 32] * 8
