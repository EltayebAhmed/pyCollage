from interfaces.private.component import Component


class DrawableComponent(Component):
    """All methods in this class are to be implemented in the concrete implementations"""
    def _get_size(self):
        """Return the size of the drawable

        :return: tuple of ints (x,y)"""
