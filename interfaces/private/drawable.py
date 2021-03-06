from interfaces.public.drawable import DrawablePublicInterface
from abc import abstractmethod

class DrawablePrivateInterface(DrawablePublicInterface):
    """All methods implemented in the drawable implementation  by developers that are not on the public interface should
    have a declaration and docstring here. All methods in this class should have names that start with a single
    underscore"""
    @abstractmethod
    def canvas(self):
        """Return the canvas the drawable is associated with.

        :return: Canvas instance
        """