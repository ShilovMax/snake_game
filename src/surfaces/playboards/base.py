from dataclasses import dataclass
import random
from drawing_objects import Grid, Apple, Snake
from utils.types import CoordsType, Action
from ..base import BaseSurface


@dataclass
class BasePlayboard(BaseSurface):
    grid: Grid
    apple: Apple
    snake: Snake
    width: int
    height: int

    def __post_init__(self) -> None:
        super().__post_init__()
        self._all_coords: set[CoordsType] = {
            (x, y) for x in range(self.width + 1) for y in range(self.height + 1)
        }

    def reset_apple(self) -> None:
        possible_apple_coords: set[CoordsType] = self._all_coords - {self.snake.coords}
        self.apple.coords = random.choice(list(possible_apple_coords))

    def do_updates(self, action: Action) -> None:
        if self._left_condition(action=action):
            self.snake.move_left()
        elif self._right_condition(action=action):
            self.snake.move_right()
        elif self._up_condition(action=action):
            self.snake.move_up()
        elif self._down_condition(action=action):
            self.snake.move_down()

    def check_game_over(self) -> bool:
        return False

    def check_win(self) -> bool:
        return self.snake.coords == self.apple.coords

    def _left_condition(self, action: Action) -> bool:
        if action == Action.left:
            if self.snake.x > 0:
                return True
        return False

    def _right_condition(self, action: Action) -> bool:
        if action == Action.right:
            if self.snake.x < self.width:
                return True
        return False

    def _up_condition(self, action: Action) -> bool:
        if action == Action.up:
            if self.snake.y > 0:
                return True
        return False

    def _down_condition(self, action: Action) -> bool:
        if action == Action.down:
            if self.snake.y < self.height:
                return True
        return False
