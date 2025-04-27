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

    def reset_on_win(self):
        for item in self.snake.body:
            item.start_coords = item.coords
        self.reset_apple(is_random=True)
        self.apple.start_coords = self.apple.coords

    def reset(self) -> None:
        self.reset_apple(is_random=False)
        self.reset_snake()

    def reset_apple(self, is_random: bool) -> None:
        if is_random:
            possible_apple_coords: set[DoubleInt] = self._all_coords - set(
                self.snake.coords
            )
            if possible_apple_coords:
                self.apple.coords = random.choice(list(possible_apple_coords))
            else:
                raise
        else:
            self.apple.reset()

    def reset_snake(self) -> None:
        self.snake.reset()

    def do_updates(self, action: Action) -> None:
        if action != Action.stay:
            print("before", self.snake)
            print(self.snake.head.coords)
            print(self.snake.body_visible_coords)
            self.snake.move(action=action)
            print("after", self.snake)
            print(self.snake.head.coords)
            print(self.snake.body_visible_coords)
            print()

    def check_game_over(self) -> bool:
        return any([
            self.snake.head.x < 0,
            self.snake.head.x > self.width,
            self.snake.head.y < 0,
            self.snake.head.y > self.height,
        ])

    def check_win(self) -> bool:
        return self.snake.head.coords == self.apple.coords
