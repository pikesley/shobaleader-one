from lib.colour_tools import complementary, drift, gamma_correct, scale_colour


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


def test_drift():
    """Test the random colour-drifter."""
    colour = [255, 255, 255]
    assert sorted(drift(colour)) == [247, 255, 255]

    colour = [32, 32, 32]
    assert sorted(drift(colour)) == [32, 32, 40]

    colour = [0, 0, 0]
    assert sorted(drift(colour)) == [0, 0, 8]
