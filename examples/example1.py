from concrete_implementation.canvashtml import CanvasHTML
from concrete_implementation.drawablehtml import DrawableHTML

class MyCanvas(CanvasHTML):
    def setup(self):
        self.queen = DrawableHTML("resources/black_queen.png", "queen")
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

c = MyCanvas()
c.display(10)