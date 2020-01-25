# from multiprocessing import Process
from lib.panel import Panel


class Shobaleader:
    """Orchestrator of the whole thing."""

    def __init__(self):
        """Construct."""
        self.panel = Panel()
        self.performer = None
        self.process = None

    def render(self, performer_class):
        """Put the frames on the panel."""
        self.performer = performer_class()
        for frame in self.performer.perform():
            self.panel.display(frame)
