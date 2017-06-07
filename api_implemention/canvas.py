from interfaces.private.canvas import CanvasPrivateInterface
import time

class Canvas(CanvasPrivateInterface):

    def __init__(self, size):
        self.size = size
        self.drawables = []
        self.backend_initialize()

    def add_drawable(self, drawable):
        self.drawables.append(drawable)

    def display(self, fps):
        time_between_frames = 1/fps
        while 1:
            start = time.time()
            self.update_frame()
            self.backend_tick()
            elapsed_time = time.time() - start
            time.sleep(max(time_between_frames - elapsed_time, 0))



