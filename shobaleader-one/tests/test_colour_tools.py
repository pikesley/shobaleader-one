from lib.colour_tools import complementary, gamma_correct, scale_colour


def test_gamma():
    """Test the gamma-correction."""
    cases = (([0, 0, 0], [0, 0, 0]), ([100, 150, 200], [19, 58, 129]))

    for colour, expected in cases:
        assert gamma_correct(colour) == expected


def test_scale():
    """Test scaling a colour."""
    cases = (
        ([255, 255, 255], 1, [255, 255, 255]),
        ([255, 127, 0], 0.5, [127, 63, 0]),
    )

    for colour, factor, expected in cases:
        assert scale_colour(colour, factor) == expected


def test_complementy():
    """Test generating complementary colours."""
    cases = (
        ([255, 255, 255], [0, 0, 0]),
        ([0, 0, 0], [255, 255, 255]),
        ([250, 128, 17], [5, 127, 238]),
    )

    for colour, expected in cases:
        assert complementary(colour) == expected
