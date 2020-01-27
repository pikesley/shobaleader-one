from abc import ABC

from lib.conf import config


class Performer(ABC):
    """Abstract Base Class for Performers."""

    def __init__(self, **kwargs):
        """Construct."""
        self.__dict__ = kwargs
        self.infinite_looping = True
        self.defaults = {"colour": config()["colours"]["orange"]}

    def apply_defaults(self):
        """Apply the default attributes."""
        for key, value in self.defaults.items():
            if not hasattr(self, key):
                setattr(self, key, value)
