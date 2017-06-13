from interfaces.private.component import Component
from abc import abstractmethod


class EventHandlerComponent(Component):
    """All methods in this class are to be implemented in the concrete implementation"""
    @abstractmethod
    def backend_tick(self):
        """Process events from backend and populate self._event_list with pyCollage events"""

    @abstractmethod
    def backend_initialize(self):
        """Run all code needed to initialize the backend event handling"""

    @abstractmethod
    def _sleep(self, time):
        """Sleep time passed in seconds while keeping the backend event loop happy and responsive

        :param time: time to sleep in seconds
        :return:
        """