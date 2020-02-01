from lib.yeeter import yeet, yeeter


def test_yeeting():
    """Test the Yeeter."""
    cases = (
        (1, 1, [(0, 0)]),
        (1, 2, [(0, 1), (0, 0)]),
        (2, 1, [(0, 0), (1, 0)]),
        (2, 2, [(0, 1), (0, 0), (1, 0)]),
        (3, 3, [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]),
    )

    for yeetee_width, grid_width, expected in cases:
        assert yeet(yeetee_width, grid_width) == expected


def test_yeeter():
    """Test the generator."""
    results = []
    for yote in yeeter(2, 6):
        results.append(yote)

    assert results == [(0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0)]


def test_reverse_yeeting():
    """Test we can go the other way."""
    cases = (
        (1, 1, [(0, 0)]),
        (1, 2, [(0, 0), (0, 1)]),
        (2, 2, [(1, 0), (0, 0), (0, 1)]),
        (3, 5, [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]),
    )

    for yeetee_width, grid_width, expected in cases:
        assert yeet(yeetee_width, grid_width, enter_from="left") == expected
