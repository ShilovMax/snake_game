from collections.abc import Iterator
from dataclasses import asdict, dataclass

from utils.types import DoubleInt


@dataclass
class BaseState:
    pass


@dataclass
class QLearningState(BaseState):
    coords: DoubleInt


@dataclass
class LinearQLearningState(BaseState):
    snake_coords: DoubleInt
    apple_coords: DoubleInt

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

    @staticmethod
    def get_all_possible_states(pow: int = 4) -> list["LessOrGreaterState"]:
        batches: list[LessOrGreaterState] = []
        n: int = 2**pow

        for i in range(n):
            val: str = bin(i)[2:]
            if len(val) < pow:
                val = "0" * (pow - len(val)) + val

            if (
                (val[0] == val[1] == "1")
                or (val[2] == val[3] == "1")
                or (val[0] == val[1] == val[2] == val[3])
            ):
                continue

            state = [bool(int(x)) for x in val]
            batches.append(LessOrGreaterState(*state))

        return batches
