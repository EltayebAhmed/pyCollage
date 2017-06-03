from abc import abstractmethod

from interfaces.private.component import Component


class ActionManagerPublicInterface(Component):
    @abstractmethod
    def report_event(self, event):
        """Report the occurrence of an event

        :param event: an instance of the Event Class
        :return: None
        """


