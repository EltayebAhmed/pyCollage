from abc import abstractmethod
from interfaces.private.drawable_component import DrawableComponent


class DrawablePublicInterface(DrawableComponent):
    """All methods on this interface are to be implemented in thi API implementation"""
    @abstractmethod
    def __init__(self, canvas, content):
        """

        :param content: path to image file
        :param name: name of drawable (string)
        """

    @abstractmethod
    def get_pos(self):
        """Return the position of the drawable

        :return: tuple of ints (x, y)
        """

    @abstractmethod
    def set_pos(self, position):
        """

        :param position: tuple of ints (x, y)
        :return: None
        """
