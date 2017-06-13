from interfaces.private.event_handler import EventHandlerPrivateInterface
from interfaces.private.events import LEFT_MOUSE_BUTTON_UP, LEFT_MOUSE_BUTTON_DOWN, MOUSE_MOTION

class EventManager(EventHandlerPrivateInterface):
    def __init__(self, canvas):
        self._handlers = {} # (drawable/canvas, event_type) : list of functions
        self._event_list = []
        self._canvas  = canvas
        self._left_mouse_down = False
        self._currently_left_clicked_item = None
    def drawable_handlers(self):
        return self._handlers.copy()

    def remove_all_event_handlers(self, drawable, event_type):
        self._handlers[(drawable, event_type)] = []

    def add_event_handler(self, component, event_type, handler):
        self._handlers[(component, event_type)] = self._handlers.get((component, event_type), [])
        self._handlers[(component, event_type)].append(handler)

    def tick(self):
        self.backend_tick()
        self._fix_mouse_events()
        self.dispatch_events()

    def dispatch_events(self):
        for event in self._event_list:
            handlers = self._handlers.get((event.owner, event.event_type), None)
            if handlers is not None:
                for handler in handlers:
                    handler(event)
        self._event_list = []

    def canvas(self):
        return self._canvas

    def _record_event(self, event):
        self._event_list.append(event)

    def _fix_mouse_events(self):
        """This function fiddles with the owners of mouse events. It ensures that every object that is that
        Receives a mouse_button_down also recieves the following mouse_button_up event and all mouse motion events
        in between"""
        for event in self._event_list:
            if event.event_type == LEFT_MOUSE_BUTTON_DOWN:
                self._left_mouse_down = True
                self._currently_left_clicked_item = event.owner
            elif event.event_type == MOUSE_MOTION and self._left_mouse_down:
                event.owner = self._currently_left_clicked_item
            elif event.event_type == LEFT_MOUSE_BUTTON_UP:
                self._currently_left_clicked_item = False
                self._currently_left_clicked_item = None
class Event:
    def __init__(self, event_type, owner, position):
        self.event_type = event_type
        self.position = position
        self.owner = owner

class MotionEvent(Event):
    def __init__(self, event_type, owner, position, displacement):
        super().__init__(event_type, owner, position)
        self.displacement = displacement
