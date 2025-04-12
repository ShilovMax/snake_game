import pygame as pg
from dataclasses import dataclass
import sys

from utils.types import ColorType


@dataclass
class BaseGame:
    caption: str
    screen_size: tuple[int, int]
    background_color: ColorType
    fps: int

    def __post_init__(self) -> None:
        pg.display.set_caption(title=self.caption)
        self.screen = pg.display.set_mode(size=self.screen_size)

        self.is_win: bool = False
        self.is_game_over: bool = False

    def play(self) -> None:
        self._draw()
        while not self.is_win and not self.is_game_over:
            self._handle_events()
            self._update()
            self._draw()
            pg.time.Clock().tick(self.fps)

    def _draw(self) -> None:
        self.screen.fill(self.background_color)
        self._draw_objects()
        pg.display.flip()

    def _draw_objects(self) -> None:
        pass

    def _handle_events(self) -> None:
        for event in pg.event.get():
            self._check_events(event=event)

    def _check_events(self, event: pg.event.Event) -> None:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    def _update(self) -> None:
        pass
