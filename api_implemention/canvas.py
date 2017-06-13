from interfaces.private.canvas import CanvasPrivateInterface
from api_implemention.event_handler import EventManager
import time

class Canvas(CanvasPrivateInterface):

    def __init__(self, size):
        self._size = size
        self._drawables = []
        self._event_manager = None # The concrete canvas will deal with this TODO make a nice import system
        self.backend_initialize()

    def add_drawable(self, drawable):
        self._drawables.append(drawable)

    def drawables(self):
        return iter(self._drawables)

    def display(self, fps):
        self.setup()
        for drawable in self._drawables:
            drawable.backend_tick()
        time_between_frames = 1/fps
        while 1:
            start = time.time()
            self._event_manager.tick()
            self.update_frame()
            self.blit_canvas()
            for drawable in self._drawables:
                drawable.backend_tick()
            self.backend_tick()
            elapsed_time = time.time() - start
            self.sleep(max(time_between_frames - elapsed_time, 0))

    def add_drawable_event_handler(self,drawable, event_type, function):
        if function is None:
            self._event_manager.remove_all_event_handlers(drawable, event_type)
        else:
            self._event_manager.add_event_handler(drawable, event_type, function)

    def sleep(self, time):
        self._event_manager._sleep(time)

    def get_position_owners(self, position):
        owners = []
        for drawable in self._drawables:
            if drawable.is_position_in_bounds(position):
                owners.append(drawable)
        if owners:
            return owners
        else:
            return [self]

