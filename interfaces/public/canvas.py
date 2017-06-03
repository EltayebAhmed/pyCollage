from abc import abstractmethod

from interfaces.private.component import Component


class CanvasPublicInterface(Component):
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
    def setup(self):
        """All user code needed to be run before the animation starts such as initializing variables

        This function should be implemented by the API user
        :return None:
        """

    @abstractmethod
    def update_frame(self):
        """All user code needed to be run to update the animation frame.

        This function should be implemented by the API user
        :return None:
        """

    @abstractmethod
    def display(self, fps):
        """Display the canvas and run the animation. NOTE this is a blocking function

        :param fps: frames per second (integer)
        :return: None
        """




