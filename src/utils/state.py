from dataclasses import dataclass

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

    def snake(self) -> QLearningState:
        return QLearningState(coords=self.snake_coords)
