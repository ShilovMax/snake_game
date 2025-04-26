from dataclasses import dataclass
import random
from drawing_objects import Grid, Apple, Snake
from utils.types import DoubleInt, Action
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
        self._all_coords: set[DoubleInt] = {
            (x, y) for x in range(self.width + 1) for y in range(self.height + 1)
        }

    def reset(self, is_random: bool) -> None:
        self.reset_apple(is_random=is_random)
        self.reset_snake()

    def reset_apple(self, is_random: bool) -> None:
        if is_random:
            possible_apple_coords: set[DoubleInt] = self._all_coords - set(
                self.snake.coords
            )

            self.apple.coords = random.choice(list(possible_apple_coords))
        else:
            self.apple.reset()

    def reset_snake(self) -> None:
        self.snake.reset()

    def do_updates(self, action: Action) -> None:
        if self._left_condition(action=action):
            self.snake.move(action=action)
        elif self._right_condition(action=action):
            self.snake.move(action=action)
        elif self._up_condition(action=action):
            self.snake.move(action=action)
        elif self._down_condition(action=action):
            self.snake.move(action=action)

    def check_game_over(self) -> bool:
        return False

    def check_win(self) -> bool:
        return self.snake.head.coords == self.apple.coords

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
