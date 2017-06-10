from api_implemention.event_handler import EventManager, Event
from interfaces.private.events import LEFT_MOUSE_BUTTON_DOWN, LEFT_MOUSE_BUTTON_UP, MOUSE_MOTION
import pygame


class EventManagerPygame(EventManager):
    def backend_initialize(self):
        pass


    def backend_tick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                 print(event)
