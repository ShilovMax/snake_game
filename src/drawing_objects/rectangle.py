from dataclasses import dataclass

from utils.types import CoordsType
from .drawing_object import AbstractXYObject
import pygame as pg
from config import CELL_SIZE


@dataclass
class Rectangle(AbstractXYObject):
    def draw(self, surface: pg.Surface) -> None:
        pg.draw.rect(
            surface,
            self.color,
            (
                self.x * CELL_SIZE,
                self.y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            ),
        )

    @property
    def coords(self) -> CoordsType:
        return self.x, self.y

    @coords.setter
    def coords(self, value: CoordsType) -> None:
        self.x, self.y = value
