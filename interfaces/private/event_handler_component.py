from interfaces.private.component import Component
from abc import abstractmethod


class EventHandlerComponent(Component):
    """All methods in this class are to be implemented in the concrete implementation"""
    @abstractmethod
    def _sleep(self, time):
        """Sleep time passed in seconds while keeping the backend event loop happy

        :param time: time to sleep in seconds
        :return:
        """