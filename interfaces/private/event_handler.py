from abc import abstractmethod
from interfaces.public.eventhandler import EventHandlerPublicInterface


class EventHandlerPrivateInterface(EventHandlerPublicInterface):
    @abstractmethod
    def __init__(self, canvas):
        pass

    @abstractmethod
    def remove_all_event_handlers(self, component, event_type):
        """Remove all event handlers associated with events of type "event_type" and owner "component" """

    @abstractmethod
    def add_event_handler(self, component, event_type, handler):
        """add a handler for events of type "event_type" and owner "component" """

    @abstractmethod
    def tick(self):
        """Execute all event related activities. To be called once per frame."""