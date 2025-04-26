from .drawing_object import AbstractDrawingObject
from utils.types import Action, DoubleInt
from .rectangle import ResetRectangle
from dataclasses import dataclass
import pygame as pg


@dataclass
class SnakeItem(ResetRectangle):
    def move_left(self) -> None:
        self.x -= 1

    def move_right(self) -> None:
        self.x += 1

    def move_up(self) -> None:
        self.y -= 1

    def move_down(self) -> None:
        self.y += 1


@dataclass
class Snake(AbstractDrawingObject):
    body: list[SnakeItem]

    def __post_init__(self) -> None:
        if len(self.body) < 1:
            raise Exception("Body couldn't be empty")

    @property
    def coords(self) -> list[DoubleInt]:
        return [x.coords for x in self.body]

    @property
    def x(self) -> int:
        return self.head.x

    @property
    def y(self) -> int:
        return self.head.y

    @property
    def head(self) -> SnakeItem:
        return self.body[0]

    def draw(self, surface: pg.Surface) -> None:
        for item in self.body:
            item.draw(surface=surface)

    def reset(self):
        for item in self.body:
            item.reset()

    def move(self, action: Action) -> None:
        new_coords_for_next_item: DoubleInt = self.head.coords
        getattr(self.body[0], f"move_{action.name}")()
        self._move_body(new_coords_for_next_item=new_coords_for_next_item)

    def _move_body(self, new_coords_for_next_item: DoubleInt) -> None:
        pass
