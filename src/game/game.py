from .base import BaseGame
from dataclasses import dataclass
from utils.types import Action
from surfaces import BasePlayboard


@dataclass
class Game[BP: BasePlayboard](BaseGame):
    playboard: BP

    def __post_init__(self) -> None:
        super().__post_init__()
        self.action: Action = Action.stay

    def play(self) -> None:
        super().play()
        if self.is_win:
            self._on_win()
        elif self.is_game_over:
            self._on_game_over()

    def _on_win(self) -> None:
        self.playboard.reset_apple()
        self.is_win = False
        self.play()

    def _on_game_over(self) -> None:
        pass

    def _draw_objects(self) -> None:
        self.playboard.draw(surface=self.screen, coords=(0, 0))

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
