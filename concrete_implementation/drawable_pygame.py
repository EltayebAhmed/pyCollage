from api_implemention.drawable import Drawable
import pygame


class DrawablePygame(Drawable):
    def backend_initialize(self):
        self.__image = pygame.image.load(self._content)

    def backend_tick(self):
        self.canvas().blit_image(self.__image, self._position)

    def _get_size(self):
        return self.__image.get_size()