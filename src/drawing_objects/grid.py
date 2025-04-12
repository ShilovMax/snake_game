from .drawing_object import DrawingObject
import pygame as pg
from config import CELL_SIZE


class Grid(DrawingObject):
    def draw(self, surface: pg.Surface) -> None:
        self.draw_vertical_lines(surface=surface)
        self.draw_horizontal_lines(surface=surface)

    def draw_vertical_lines(self, surface: pg.Surface) -> None:
        for i in range(1, self.x):
            pg.draw.line(
                surface,
                self.color,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, self.y * CELL_SIZE),
            )

    def draw_horizontal_lines(self, surface: pg.Surface) -> None:
        for i in range(1, self.y):
            pg.draw.line(
                surface,
                self.color,
                (0, i * CELL_SIZE),
                (self.x * CELL_SIZE, i * CELL_SIZE),
            )
