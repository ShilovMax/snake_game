from .base import BaseGame
from dataclasses import dataclass
from utils.types import Action
from surfaces import BasePlayboard, ScoreSurface
import pygame as pg


@dataclass
class Game[BP: BasePlayboard](BaseGame):
    playboard: BP
    score_surface: ScoreSurface

    def __post_init__(self) -> None:
        super().__post_init__()
        self.action: Action = Action.stay
        self.score: int = 0

    @property
    def snake(self):
        return self.playboard.snake

    @property
    def snake_head(self):
        return self.playboard.snake.head

    @property
    def apple(self):
        return self.playboard.apple

    def play(
        self,
        endless_win: bool,
        endless_lose: bool,
        sleep: float = 0,
    ) -> None:
        self.endless_win = endless_win
        self.endless_lose = endless_lose
        self.sleep = sleep
        super().play(sleep=sleep)
        if self.is_win:
            self._on_win()
        elif self.is_game_over:
            self._on_game_over()

    def _on_win(self) -> None:
        self._reset()
        self.is_win = False
        self._update_score()
        if self.endless_win:
            self.play(
                endless_win=self.endless_win,
                endless_lose=self.endless_lose,
                sleep=self.sleep,
            )

    def _reset(self) -> None:
        try:
            self.playboard.reset_on_win()
        except Exception:
            print("EXCEPTION")
            self.is_game_over = True

    def _update_score(self):
        self.score += 1
        self.score_surface.text = self.score_surface.text.split()[0] + f" {self.score}"

    def _on_game_over(self) -> None:
        print("on game over")
        self.playboard.reset()
        self.is_game_over = False
        if self.endless_lose:
            self.play(
                endless_win=self.endless_win,
                endless_lose=self.endless_lose,
                sleep=self.sleep,
            )

    def _draw_objects(self) -> None:
        self.score_surface.draw(
            surface=self.screen, coords=(0, 0), rect=self._get_rect_for_score()
        )
        self.playboard.draw(surface=self.screen, coords=(0, self.score_surface.height))

    def _get_rect_for_score(self) -> pg.Rect:
        return self.score_surface.rect(
            center=(self.screen_size[0] // 2, self.score_surface.height // 2)
        )

    def _update(self) -> None:
        self._do_updates()
        self._check_game_over()
        self._check_win()
        self.action = Action.stay

    def _do_updates(self) -> None:
        self.playboard.do_updates(action=self.action)

    def _check_game_over(self) -> None:
        self.is_game_over = self.playboard.check_game_over()

    def _check_win(self) -> None:
        self.is_win = self.playboard.check_win()
