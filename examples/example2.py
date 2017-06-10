# A drag/snap board

from concrete_implementation.canvas_pygame import CanvasPygame
from concrete_implementation.drawable_pygame import DrawablePygame
from interfaces.private.events import LEFT_MOUSE_BUTTON_DOWN

class MyCanvas(CanvasPygame):
    def setup(self):
        self.queen = DrawablePygame(self, "resources/black_queen.png")
        #self.queen.make_draggable()
        self.queen.add_event_handler(LEFT_MOUSE_BUTTON_DOWN,self.snap)

    def update_frame(self):
        return
    def snap(self):
        old_position = self.queen.get_pos()
        new_position = map(lambda x:(x//25)*25, old_position)
        self.queen.set_pos(new_position)

c = MyCanvas((400, 400))
c.display(30)