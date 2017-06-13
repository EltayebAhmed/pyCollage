from abc import abstractmethod
from interfaces.public.eventhandler import EventHandlerPublicInterface


class EventHandlerPrivateInterface(EventHandlerPublicInterface):
    @abstractmethod
    def drawable_handlers(self):
        """"""