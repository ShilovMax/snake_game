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

    def play(self, endless: bool, sleep: float = 0) -> None:
        super().play(sleep=sleep)
        if self.is_win:
            self._on_win(endless=endless, sleep=sleep)
        elif self.is_game_over:
            self._on_game_over()

    def _on_win(self, endless: bool, sleep: float) -> None:
        self._reset()
        self.is_win = False
        self._update_score()
        if endless:
            self.play(endless=endless, sleep=sleep)

    def _reset(self) -> None:
        self.playboard.reset_apple(is_random=True)

    def _update_score(self):
        self.score += 1
        self.score_surface.text = self.score_surface.text.split()[0] + f" {self.score}"

    def _on_game_over(self) -> None:
        pass

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
