from api_implemention.event_handler import EventManager, Event, MotionEvent
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
                    event_type = LEFT_MOUSE_BUTTON_UP
                    position = event.pos
            elif event.type == pygame.MOUSEMOTION:
                event_type = MOUSE_MOTION
                position = event.pos
            elif event.type == pygame.QUIT:
                quit()
            if event_type is not None:
                if position is not None:
                    owners = self.canvas().get_position_owners(position)
                    for owner in owners:
                        if event_type == MOUSE_MOTION:
                            i = list(map(lambda x: isinstance(x, MotionEvent), self._event_list))
                            if not any(i):
                                e = MotionEvent(MOUSE_MOTION, owner, position, displacement=event.rel)
                                self._record_event(e)
                            else:
                                i = i.index(True)
                                old_event = self._event_list[i]
                                displacement = old_event.displacement[0] + event.rel[0], \
                                                    old_event.displacement[1] + event.rel[1]
                                new_event = MotionEvent(MOUSE_MOTION, old_event.owner,position, displacement)

                                self._event_list[i] = new_event
                        else:
                            e = Event(event_type, owner, position)
                            self._record_event(e)


    def _sleep(self, time):
        pygame.time.wait(int(time*1e3))