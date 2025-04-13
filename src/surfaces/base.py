from dataclasses import dataclass
import pygame as pg
from drawing_objects import AbstractDrawingObject
from utils.types import ColorType


@dataclass
class BaseSurface:
    size: tuple[int, int]
    background_color: ColorType

    def __post_init__(self):
        self.surface: pg.Surface = pg.Surface(size=self.size)
        self.drawing_objects: list[AbstractDrawingObject] = []
        self._set_drawing_objects()

    def _set_drawing_objects(self) -> None:
        attrs = self.__dict__.copy()
        for attr in attrs:
            attr_ = getattr(self, attr)
            self._check_drawing_attr(attr=attr_)

    def _check_drawing_attr(self, attr) -> None:
        if isinstance(attr, AbstractDrawingObject):
            self.drawing_objects.append(attr)

    def draw(self, surface: pg.Surface, coords: tuple[int, int], **kwargs) -> None:
        self.surface.fill(color=self.background_color)
        self._draw_objects(**kwargs)
        surface.blit(self.surface, coords)

    def _draw_objects(self, **kwargs) -> None:
        for obj in self.drawing_objects:
            obj.draw(surface=self.surface, **kwargs)
