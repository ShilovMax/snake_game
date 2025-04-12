from .base import BaseGame
from dataclasses import dataclass
from drawing_objects import Apple, Snake, Grid
from action import Action


@dataclass
class Game(BaseGame):
    apple: Apple
    snake: Snake
    grid: Grid
    width: int
    height: int

    def __post_init__(self) -> None:
        super().__post_init__()
        self.action: Action = Action.stay

    def _draw_objects(self) -> None:
        self.apple.draw(surface=self.screen)
        self.snake.draw(surface=self.screen)
        self.grid.draw(surface=self.screen)

    def _update(self) -> None:
        self._do_updates()
        self._check_game_over()
        self._check_win()
        self.action = Action.stay

    def _do_updates(self) -> None:
        if self.action == Action.left:
            if self.snake.x > 0:
                self.snake.move_left()

        elif self.action == Action.right:
            if self.snake.x < self.width - 1:
                self.snake.move_right()

        elif self.action == Action.up:
            if self.snake.y > 0:
                self.snake.move_up()

        elif self.action == Action.down:
            if self.snake.y < self.height - 1:
                self.snake.move_down()

    def _check_game_over(self) -> None:
        self.is_game_over = False

    def _check_win(self) -> None:
        self.is_win = self.apple.coords == self.snake.coords
