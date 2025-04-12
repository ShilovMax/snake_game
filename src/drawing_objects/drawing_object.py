import pygame as pg
from dataclasses import dataclass
from config import CELL_SIZE
from utils.types import ColorType


@dataclass
class DrawingObject:
    x: int
    y: int
    color: ColorType

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
