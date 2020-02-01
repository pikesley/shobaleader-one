from multiprocessing import Process

from lib.panel import Panel


class Shobaleader:
    """Orchestrator of the whole thing."""

    def __init__(self):
        """Construct."""
        self.panel = Panel()
        self.performer_class = None
        self.args = None
        self.process = None

    def render(self):
        """Put the frames on the panel."""
        performer = self.performer_class(**self.args)
        for frame in performer.perform():
            self.panel.display(frame)

    def run(self, performer_class, **kwargs):
        """Control the process."""
        if performer_class == self.performer_class and kwargs == self.args:
            return  # nocov

        self.performer_class = performer_class
        self.args = kwargs
        self.stop()

        self.process = Process(target=self.render)
        self.process.start()

    def stop(self):
        """Stop the running process."""
        if self.process:
            self.process.terminate()
