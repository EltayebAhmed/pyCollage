from abc import ABC, abstractmethod

class Component(ABC):
    """All methods in this class are to be implemented in the concrete implementations"""
    @abstractmethod
    def backend_tick(self):
        """Run all backend code related to backend code needed to update the frame
        Will be called every once every animation frame"""

    @abstractmethod
    def engine_initialize(self):
        """Run all backend code related to backend code needed to initialize the animation
        Will be called once before the animation starts"""