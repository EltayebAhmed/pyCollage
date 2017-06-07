from api_implemention.canvas import Canvas
import pygame

class CanvasPygame(Canvas):
    def backend_initialize(self):
        pygame.init()
        self.__display = pygame.display.set_mode(self.size)


    def backend_tick(self):
        pygame.display.flip()