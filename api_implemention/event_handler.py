from interfaces.private.event_handler_component import EventHandlerComponent


class EventManager(EventHandlerComponent):
    def __init__(self, canvas):
        self._drawable_handlers = {} # (drawable/canvas, event_type) : list of functions
        self._event_list = []
        self._canvas  = canvas

    def drawable_handlers(self):
        return self._drawable_handlers.copy()

    def remove_drawable_event_handler(self, drawable, event_type):
        self._drawable_handlers[(drawable, event_type)] = []

    def add_drawable_event_handler(self, drawable, event_type, handler):
        self._drawable_handlers[(drawable, event_type)] = self._drawable_handlers.get((drawable, event_type),[])
        self._drawable_handlers[(drawable, event_type)].append(handler)

    def tick(self):
        self.backend_tick()
        self.dispatch_events()

    def dispatch_events(self):
        for event in self._event_list:
            handlers = self._drawable_handlers.get((event.owner, event.event_type ), None)
            if handlers is not None:
                for handler in handlers:
                    handler(event)
        self._event_list = []

    def canvas(self):
        return self._canvas
    def _record_event(self, event):
        self._event_list.append(event)


class Event:
    def __init__(self, event_type, owner, position):
        self.event_type = event_type
        self.position = position
        self.owner = owner