from abc import ABC, abstractmethod


class DrawableInterface(ABC):
    @abstractmethod
    def apply_config(self, drawable_config):
        """
        Apply changes in drawable_config to self
        :param drawable_config: An instance of _Drawable_config
        :return: ErrorCode, 0 is successful
        """