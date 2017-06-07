from interfaces.private.drawable import DrawablePrivateInterface


class Drawable(DrawablePrivateInterface):
    def set_pos(self, position):
        super().set_pos(position)