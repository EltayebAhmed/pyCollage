from interfaces.private.component import Component

class EventManager(Component):
    def __init__(self):
        self._drawable_handlers = {} # (drawable/canvas, event_type) : list of functions
        self._event_list = []

    def drawable_handlers(self):
        return self._drawable_handlers.copy()

    def remove_drawable_event_handler(self, drawable, event_type):
        self._drawable_handlers[(drawable, event_type)] = []

    def add_drawable_event_handler(self, drawable, event_type, handler):
        self._drawable_handlers[(drawable, event_type)] = self._drawable_handlers.get((drawable, event_type),[])
        self._drawable_handlers[(drawable, event_type)].append(handler)

class Event:
    def __init__(self, event_type, coordinates):
        self.event_type = event_type
        self.coordinates = coordinates