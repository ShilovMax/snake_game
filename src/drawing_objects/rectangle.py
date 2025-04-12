from dataclasses import dataclass

from utils.types import CoordsType
from .drawing_object import DrawingObject


@dataclass
class Rectangle(DrawingObject):
    @property
    def coords(self) -> CoordsType:
        return self.x, self.y
