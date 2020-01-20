from lib.performers.simple import SimplePerformer


class TestSimple:
    """Test the SimplePerformer."""

    def test_iterator(self):
        """Test it implements an iterator."""
        simp = SimplePerformer()

        results = []

        count = 0
        for item in simp.perform():
            results.append(item)
            count += 1
            if count > 1:
                break

        assert results[0] == [[[0, 0, 0]] * 32] * 8
        assert results[1] == [[[255, 0, 0]] * 32] * 8
