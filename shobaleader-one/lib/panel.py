import lib.conf


class Panel:
    """Class representing the Longruner light panel."""

    def __init__(self):
        """Construct."""
        self.config = lib.conf.config()['panel']
        self.width = self.config['width']
        self.height = self.config['height']
        self.length = self.width * self.height

