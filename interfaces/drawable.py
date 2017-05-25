from abc import ABC, abstractmethod


POSITION = 100012
class DrawableInterface(ABC):
    @abstractmethod
    def query(self, query_type):
        pass

    @abstractmethod
    def execute_action(self, action):
        pass

    @abstractmethod
    def tick(self):
        pass