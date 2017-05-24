from abc import ABC,abstractmethod


class Canvas(ABC):
    @abstractmethod
    def add_drawable(self, drawable_content, drawable_config):
        """
        An function to create and add a new drawable to the GUI Canvas
        :param drawable_content: a python file object that contains a jpeg OR
            as a string that contains plain text
        :param drawable_config:  a python dictionary. IS CURRENTLY USELESS
        :return: None
        """

    @abstractmethod
    def drawables(self):
        """
        An iterator over all drawables
        :return: Iterator over all drawables
        """
