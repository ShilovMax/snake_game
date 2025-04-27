from .drawing_object import AbstractDrawingObject
from utils.types import Action, DoubleInt, TripleInt
from .rectangle import ResetRectangle
from dataclasses import dataclass
import pygame as pg


@dataclass
class SnakeItem(ResetRectangle):
    is_visible: bool

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
    def body_visible_coords(self) -> list[DoubleInt]:
        return [x.coords for x in self.body[1:] if x.is_visible]

    @property
    def head(self) -> SnakeItem:
        return self.body[0]

    @property
    def tail(self) -> SnakeItem:
        return self.body[-1]

    def draw(self, surface: pg.Surface) -> None:
        for item in self.body:
            item.draw(surface=surface)

    def reset(self):
        new_coords = []
        for item in self.body:
            item.reset()
            if item.coords in new_coords:
                item.is_visible = False
            new_coords.append(item.coords)

    def move(self, action: Action) -> None:
        new_coords_for_next_item: DoubleInt = self.head.coords
        getattr(self.head, f"move_{action.name}")()
        self._move_body(new_coords_for_next_item=new_coords_for_next_item)

    def add_item(
        self,
        x: int | None = None,
        y: int | None = None,
        color: TripleInt | None = None,
        is_visible: bool = True,
    ):
        item: SnakeItem = SnakeItem(
            x=x if x is not None else self.tail.x,
            y=y if y is not None else self.tail.y,
            color=color if color is not None else self._get_new_item_color(),
            is_visible=is_visible,
        )
        self.body.append(item)

    def _move_body(self, new_coords_for_next_item: DoubleInt) -> None:
        for item in self.body[1:]:
            if item.is_visible is False:
                item.is_visible = True
            item_coords: DoubleInt = item.coords
            item.x, item.y = new_coords_for_next_item
            new_coords_for_next_item = item_coords

    def _get_new_item_color(self) -> TripleInt:
        return TripleInt(c - 5 if c > 5 else c for c in self.tail.color)
