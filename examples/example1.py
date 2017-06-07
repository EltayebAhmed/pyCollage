from concrete_implementation.canvas_pygame import CanvasPygame
from concrete_implementation.drawable_pygame import DrawablePygame

class MyCanvas(CanvasPygame):
    def setup(self):
        self.queen = DrawablePygame(self, "resources/black_queen.png")
        self.add_drawable(self.queen)
        self.queen.set_pos((100,100))
        self.steps = 0
        self.direction = 1

    def update_frame(self):
        old_pos = self.queen.get_pos()
        new_pos = (old_pos[0]+self.direction, old_pos[1])
        self.steps += self.direction
        if abs(self.steps) == 50:
            self.direction *= -1
        self.queen.set_pos(new_pos)

c = MyCanvas((500,500))
c.display(30)