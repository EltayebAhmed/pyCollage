from api_implemention.canvas import Canvas
from concrete_implementation.event_handler_pygame import EventManagerPygame
import pygame

class CanvasPygame(Canvas):
    def backend_initialize(self):
        pygame.init()
        self.__display = pygame.display.set_mode(self._size)
        self._event_manager = EventManagerPygame()

    def backend_tick(self):
        pygame.display.flip()

    def blit_image(self, image, position):
        self.__display.blit(image, position)

    def blit_canvas(self):
          self.__display.fill((255, 255, 255))