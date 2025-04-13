from dataclasses import dataclass

import pygame as pg

from drawing_objects import TextObject

from ..base import BaseSurface


pg.font.init()


@dataclass
class ScoreSurface(BaseSurface):
    score: TextObject

    def rect(self, center) -> pg.Rect:
        return self.score.text_surface.get_rect(center=center)

    @property
    def height(self) -> int:
        return self.score.rect_size[1]

    @property
    def text(self) -> str:
        return self.score.text

    @text.setter
    def text(self, value: str) -> None:
        self.score.text = value
