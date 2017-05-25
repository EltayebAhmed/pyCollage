from abc import ABC, abstractmethod

class _DrawableConfigInterface(ABC):
    """All messages between Canvas and Drawable are passed as instances of this class

    All coordinates are in Canvas space"""
    @abstractmethod
    def get_pos(self):
        """Get the position of the top left corner of the canvas relative to top left corner of canvas

        :return: tuple (integer_width, integer_height)
        """
        pass

    @abstractmethod
    def set_pos(self, position):
        """

        :param position: tuple (integer_width, integer_height)
        :return: None
        """
