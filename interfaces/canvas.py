from abc import ABC,abstractmethod


class CanvasInterface(ABC):
    @abstractmethod
    def add_drawable(self, drawable):
        """Add a new drawable to the  Canvas
        :param drawable: An instance of class drawable
        :return: None
        """

    @abstractmethod
    def drawables(self):
        """Returns an iterator over all drawables

        :return: Iterator over all drawables
        """

    @abstractmethod
    def display(self):
        """Display the canvas. NOTE this is a blocking function

        :return: Error code, 0 if successful
        """

    @abstractmethod
    def execute_action(self, action):
        """Perfom canvas action (e.g. close, minimize, ...) in the passed action instance

        :param action:  Instance of Action
        :return: None
        """
        pass

    @abstractmethod
    def canvas_init(self):
        """Initialize the canvas's backend"""

    @bas