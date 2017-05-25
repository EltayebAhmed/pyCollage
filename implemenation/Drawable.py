from interfaces.drawable import DrawableInterface
import pygame
import os.path

class Drawable(DrawableInterface):
    def __init__(self, canvas, content):
        self._position = (0, 0)
        self._size = (10,10)
        self.canvas = canvas
        assert (isinstance(content, str))
        # ===========================
        if 1:# check that content is jpeg file path
            self.image = pygame.image.load(content)


        elif isinstance(content, str):
            raise NotImplementedError()


    def apply_config(self, drawable_config):
        config_pos = drawable_config.get_pos()
        if config_pos is not None:
            pass

