from lib.performers.performer import Performer


class TestPerformert:
    """Test the Performer."""

    def test_constructor(self):
        """Test it gets the right attributes."""

        data = {"foo": "bar"}
        perf = Performer(**data)

        assert perf.foo == "bar"
        assert perf.infinite_looping
