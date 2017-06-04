from abc import abstractmethod
from interfaces.private.component import Component


class DrawablePublicInterface(Component):
    @abstractmethod
    def __init__(self, content):
        """

        :param content: path to jpeg image
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
