from abc import abstractmethod
from interfaces.private.component import Component


class DrawablePublicInterface(Component):
    @abstractmethod
    def __init__(self):
        re

    @abstractmethod
    def get_pos(self):
        """Return the position of the drawable"""
