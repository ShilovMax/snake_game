from dataclasses import dataclass

from utils.types import Action, DoubleInt

from .base import BasePlayboard


@dataclass
class LongSnakePlayboard(BasePlayboard):
    def __post_init__(self) -> None:
        super().__post_init__()
        self.previous_snake_coords: list[DoubleInt] = []

    def check_win(self) -> bool:
        if win := super().check_win():
            self.snake.add_item(is_visible=False)
        return win

    def check_game_over(self) -> bool:
        return (
            self.snake.head.coords in self.snake.body_visible_coords
            or super().check_game_over()
            or self.previous_snake_coords == self.snake.coords[::-1]
        )

    def do_updates(self, action: Action) -> None:
        if action != Action.stay:
            self.previous_snake_coords = (
                self.snake.coords if len(self.snake.coords) == 2 else []
            )
            print("befaroe", self.snake.coords)
            self.snake.move(action=action)
            print("after", self.snake.coords)
            print(self.snake.head.coords, self.snake.body_visible_coords)
