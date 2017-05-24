from abc import ABC,abstractmethod


class CanvasInterface(ABC):
    @abstractmethod
    def add_drawable(self, drawable_content, drawable_config):
        """A function that creates and adds a new Drawable to the  Canvas

        :param drawable_content: a python file object that contains a jpeg OR
            as a string that contains plain text
        :param drawable_config:  a python dictionary. IS CURRENTLY USELESS
        :return: None
        """

    @abstractmethod
    def drawables(self):
        """An iterator over all drawables

        :return: Iterator over all drawables
        """

    @abstractmethod
    def display(self):
        """Display the canvas. NOTE this is a blocking function

        :return: Error code, 0 if successful
        """