from abc import ABC, abstractmethod


class ActionManagerInterface(ABC):
    @abstractmethod
    def report_event(self, event):
        """Report the occurence of an event

        :param event: an instance of the Event Class
        :return: None
        """

    @abstractmethod
    def tick(self):
        """Must be called every once every game cylce."""
