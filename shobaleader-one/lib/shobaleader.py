# from multiprocessing import Process


class Shobaleader:
    """Orchestrator of the whole thing."""

    def __init__(self, panel):
        """Construct."""
        self.panel = panel
        self.performer = None
        self.process = None

    # def render(self, performer_class):
    #     """Put the frames on the panel."""
    #     self.performer = performer_class()
    #     for frame in self.performer.perform():
    #         self.panel.display(frame)

