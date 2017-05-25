from abc import ABC, abstractmethod
from interfaces.Canvas import CanvasInterface
from implemenation.Drawable import Drawable
from implemenation._DrawableConfig import _DrawableConfig

class Canvas(CanvasInterface):
    def __init__(self):
        self._drawables = []

    def drawables(self):
        return iter(self._drawables)

    def add_drawable(self, drawable_content, drawable_config):
        drawable = Drawable(self, drawable_content)
        drawable.apply_config(drawable_config)
        self._drawables.append(drawable)

    def display(self):
        import pygame
        pygame.init()
        from pygame import QUIT
        screen = pygame.display.set_mode((400,400))
        screen.fill([255,255,255])

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type ==QUIT:
                    done = True
            for drawable in self.drawables():
                screen.blit(drawable.image,(0,0))

            pygame.display.flip()


c = Canvas()
im_path = (r"C:\Users\eltay\PycharmProjects\gui2draw\resources\black_queen.png")
c.add_drawable(im_path,_DrawableConfig())
c.display()