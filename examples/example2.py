# A drag/snap board

from concrete_implementation.canvas_pygame import CanvasPygame
from concrete_implementation.drawable_pygame import DrawablePygame
from interfaces.private.events import LEFT_MOUSE_BUTTON_UP

class MyCanvas(CanvasPygame):
    def setup(self):
        self.queen = DrawablePygame(self, "resources/black_queen.png")
        self.queen.make_draggable()
        self.queen.add_event_handler(LEFT_MOUSE_BUTTON_UP,self.snap)
        self.add_drawable(self.queen)
        self.queen.set_pos((149,149))

    def update_frame(self):
        return
    def snap(self, event):
        old_position = self.queen.get_pos()
        new_position = map(lambda x:(x//25)*25, old_position)
        new_position = tuple(new_position)
        self.queen.set_pos(new_position)

c = MyCanvas((400, 400))
c.display(30)