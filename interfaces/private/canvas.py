from interfaces.public.canvas import CanvasPublicInterface
from abc import abstractmethod


class CanvasPrivateInterface(CanvasPublicInterface):
    """All methods implemented in the canvas implementation  by developers that are not on the public interface should
    have a declaration and docstring here. All methods in this class should have names that start with a single
    underscore"""
    @abstractmethod
    def add_drawable_event_handler(self,drawable, event_type, function):
        """The function passed will be called on event of types event type. set function=None to unset all handlers"""
