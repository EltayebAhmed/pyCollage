from interfaces.private.drawable import DrawablePrivateInterface


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

