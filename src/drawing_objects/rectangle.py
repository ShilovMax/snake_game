from .drawing_object import DrawingObject


class Rectangle(DrawingObject):
    @property
    def coords(self) -> tuple[int, int]:
        return self.x, self.y
