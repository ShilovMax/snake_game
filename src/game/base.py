import pygame as pg
from dataclasses import dataclass
import sys
import time
from utils.types import DoubleInt, TripleInt


@dataclass
class BaseGame:
    caption: str
    screen_size: DoubleInt
    background_color: TripleInt
    fps: int

    def __post_init__(self) -> None:
        pg.display.set_caption(title=self.caption)
        self.screen = pg.display.set_mode(size=self.screen_size)

        self.is_win: bool = False
        self.is_game_over: bool = False
        self.is_pause: bool = False

    def play(self, sleep: float = 0) -> None:
        self._draw()
        while not self.is_win and not self.is_game_over:
            self._handle_events()
            if not self.is_pause:
                self._update()
                self._draw()
                pg.time.Clock().tick(self.fps)
                if sleep:
                    time.sleep(sleep)

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
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                self.is_pause = not self.is_pause

    def _update(self) -> None:
        pass
