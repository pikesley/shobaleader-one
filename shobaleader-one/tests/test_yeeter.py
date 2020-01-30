from lib.yeeter import yeet

def test_yeeting():
    """Test the Yeeter."""
    cases = (
        (1, 1, [(0, 0)]),
        (1, 2, [(0, 1), (0, 0)]),
        (2, 1, [(0, 0), (1, 0)]),
        (2, 2, [(0, 1), (0, 0), (1, 0)]),
        (3, 3, [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    )

    for yeetee_width, grid_width, expected in cases:
        assert yeet(yeetee_width, grid_width) == expected
