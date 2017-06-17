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

    def get_size(self):
        """Return the size of the drawable

        :return: tuple of ints (x,y)"""

    def set_size(self, size):
        """Set the size of the drawable

        :param size: tuple of ints (x, y)
        :return: None
        """
    @abstractmethod
    def set_pos(self, position):
        """Set the position of the drawable to "position"

        :param position: tuple of ints (x, y)
        :return: None
        """

    @abstractmethod
    def is_position_in_bounds(self, position):
        """Return True if position is in bounds of this drawable, False otherwise"""

    @abstractmethod
    def add_event_handler(self, event_type, function):
        """The function passed will be called on event of types event type. set function=None to unset all handlers"""

    @abstractmethod
    def make_draggable(self):
        """Make the drawable draggable with the left mouse click"""