from interfaces.private.drawable import DrawablePrivateInterface
from interfaces.private.events import LEFT_MOUSE_BUTTON_UP, LEFT_MOUSE_BUTTON_DOWN,MOUSE_MOTION

class Drawable(DrawablePrivateInterface):
    def __init__(self, canvas, content):
        self._content = content
        self._canvas = canvas
        self._position = (0,0)
        self.backend_initialize()

    def get_pos(self):
        return self._position

    def set_pos(self, position):
        assert type(position) == tuple
        assert len (position) == 2
        assert all(map(lambda x : type(x)==int and x>=0, position))
        self._position = position

    def get_size(self):
        return self._get_size()

    def canvas(self):
        return self._canvas

    def is_position_in_bounds(self, position):
        x_pos, y_pos = self.get_pos()
        x_size, y_size = self.get_size()
        x_in_bounds = x_pos <= position[0] <= x_pos +  x_size
        y_in_bounds = y_pos <= position[1] <= y_pos + y_size
        return x_in_bounds and y_in_bounds

    def add_event_handler(self, event_type, function):
        self.canvas().add_drawable_event_handler(self, event_type, function)
#===================================================================================
    # COMPOSITE EVENTS
    def make_draggable(self):
        self.add_event_handler(LEFT_MOUSE_BUTTON_DOWN, self._handler_start_drag)

    def _handler_start_drag(self, event):

        def _handler_follow_mouse(event):
            self.set_pos(event.position) # TODO add displacement to MOUSE_MOTION events. Document it then use it here
        def _handler_stop_follow_mouse(event):
            self.add_event_handler(MOUSE_MOTION, None)
        self.add_event_handler(MOUSE_MOTION, _handler_follow_mouse)
        self.add_event_handler(LEFT_MOUSE_BUTTON_UP, _handler_stop_follow_mouse)








