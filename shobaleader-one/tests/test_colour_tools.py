from lib.colour_tools import gamma_correct, scale_colour


def test_gamma():
    """Test the gamma-correction."""
    cases = (((0, 0, 0), [0, 0, 0]), ((100, 150, 200), [19, 58, 129]))

    for case in cases:
        assert gamma_correct(case[0]) == case[1]


def test_scale():
    """Test scaling a colour."""
    cases = (
        ((255, 255, 255), 1, [255, 255, 255]),
        ((255, 127, 0), 0.5, [127, 63, 0]),
    )

    for case in cases:
        assert scale_colour(case[0], case[1]) == case[2]
