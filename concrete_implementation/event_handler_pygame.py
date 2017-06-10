from api_implemention.event_handler import EventManager, Event
from interfaces.private.events import LEFT_MOUSE_BUTTON_DOWN, LEFT_MOUSE_BUTTON_UP, MOUSE_MOTION
import pygame


class EventManagerPygame(EventManager):

    def backend_initialize(self):
        pass

    def backend_tick(self):
        for event in pygame.event.get():
            event_type = None
            position = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    event_type = LEFT_MOUSE_BUTTON_DOWN
                    position = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    event_type = LEFT_MOUSE_BUTTON_DOWN
                    position = event.pos
            elif event.type == pygame.MOUSEMOTION:
                event_type = MOUSE_MOTION
                position = event.pos
            if event_type is not None:
                if position is not None:
                    owners = self.canvas().get_position_owners(position)
                    for owner in owners:
                        e = Event(event_type, owner, position)
                        self._record_event(e)
                else:
                    e = Event(event_type,self.canvas(), None) #TODO handle this
                    print ("Canvas events not implemented")
                    #self._record_event()

    def _sleep(self, time):
        pygame.time.wait(int(time*1e3))