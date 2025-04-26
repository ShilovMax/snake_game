import pygame as pg
from dataclasses import dataclass

from utils.types import DoubleInt
from .drawing_object import AbstractDrawingObject, ColorMixin


@dataclass
class TextObject(AbstractDrawingObject, ColorMixin):
    font_size: int
    rect_size: DoubleInt
    _text: str

    def __post_init__(self):
        self.font = pg.font.SysFont(None, self.font_size)
        self._post_init()

    def draw(self, surface: pg.Surface, rect: pg.Rect) -> None:
        if rect:
            surface.blit(self.text_surface, rect)

    def _post_init(self):
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_surface = pg.transform.scale(self.text_surface, self.rect_size)

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._post_init()
