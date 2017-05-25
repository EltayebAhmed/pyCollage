from interfaces._DrawableConfig import _DrawableConfigInterface



class _DrawableConfig(_DrawableConfigInterface):
    def __init__(self):
        self._position = None
        self._size = None

    def set_pos(self, position):
        assert isinstance(position, tuple)
        assert len(position) == 2
        assert 0 <= position[0] <= 1000
        assert 0 <= position[1] <= 1000
        self._position = position

    def get_pos(self):
        return self._position
