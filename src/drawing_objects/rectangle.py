from dataclasses import dataclass

from utils.types import DoubleInt
from .drawing_object import AbstractDrawingObject, ColorMixin, XYMixin
import pygame as pg
from config import CELL_SIZE


@dataclass
class Rectangle(AbstractDrawingObject, ColorMixin, XYMixin):
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
    def coords(self) -> DoubleInt:
        return self.x, self.y

    @coords.setter
    def coords(self, value: DoubleInt) -> None:
        self.x, self.y = value


@dataclass
class ResetRectangle(Rectangle):
    def __post_init__(self) -> None:
        self.start_coords: DoubleInt = (self.x, self.y)

    def reset(self) -> None:
        self.x, self.y = self.start_coords
