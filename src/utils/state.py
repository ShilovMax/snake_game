from collections.abc import Iterator
from dataclasses import asdict, dataclass

from utils.types import CoordsType


@dataclass
class BaseState:
    pass


@dataclass
class QLearningState(BaseState):
    coords: CoordsType


@dataclass
class LinearQLearningState(BaseState):
    snake_coords: CoordsType
    apple_coords: CoordsType

    def get_linear_coords(self, size: int) -> QLearningState:
        return QLearningState(
            coords=(
                self.snake_coords[0] * size + self.snake_coords[1],
                self.apple_coords[0] * size + self.apple_coords[1],
            ),
        )


@dataclass
class LessOrGreaterState(BaseState):
    is_head_x_less_than_apple_x: bool
    is_head_x_greater_than_apple_x: bool
    is_head_y_less_than_apple_y: bool
    is_head_y_greater_than_apple_y: bool

    def __iter__(self) -> Iterator[int]:
        return iter([int(x) for x in asdict(self).values()])
