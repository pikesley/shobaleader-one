from lib.text_banner import TextBanner


class TestTextBanner:
    """Test the TextBanner."""

    def test_constructor(self):
        """Test it gets the right data."""
        banner = TextBanner("E8 Boogie")

        assert banner.text == "E8 Boogie"
        assert banner.width == 55
        assert banner.font[" "] == [[0] * 6] * 8

    def test_griddling(self):
        """Test it turns the text into a grid."""
        banner = TextBanner("abc")

        assert banner.grid == [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def test_carving(self):
        """Test it chops up nicely."""
        banner = TextBanner("E8 Boogie")

        assert banner.carve_slice(x_index=7, width=6) == [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]
