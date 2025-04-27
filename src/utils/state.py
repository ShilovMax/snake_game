from collections.abc import Iterator
from dataclasses import asdict, dataclass
from typing import Self
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


# @dataclass
@dataclass
class LessOrGreaterState(BaseState):
    is_head_x_less_than_apple_x: bool
    is_head_x_greater_than_apple_x: bool
    is_head_y_less_than_apple_y: bool
    is_head_y_greater_than_apple_y: bool

    def __iter__(self) -> Iterator[int]:
        return iter([int(x) for x in asdict(self).values()])

    @classmethod
    def get_all_possible_states(cls) -> list[Self]:
        batches: list[Self] = []
        pow = len(cls.__dataclass_fields__)
        n: int = 2**pow

        for i in range(n):
            val: str = bin(i)[2:]
            if len(val) < pow:
                val = "0" * (pow - len(val)) + val

            if cls._check_value(val=val):
                continue

            state = [bool(int(x)) for x in val]
            batches.append(cls(*state))

        return batches

    @classmethod
    def _check_value(cls, val: str) -> bool:
        return (
            (val[0] == val[1] == "1")
            or (val[2] == val[3] == "1")
            or (val[0] == val[1] == val[2] == val[3])
        )


@dataclass
class PlusShapedVisionState:
    is_barrier_on_left: bool = False
    is_barrier_on_right: bool = False
    is_barrier_on_top: bool = False
    is_barrier_on_bottom: bool = False


@dataclass
class PlusShapedVisionLessOrGreateStateState(PlusShapedVisionState, LessOrGreaterState):
    # @classmethod
    # def get_all_possible_states(cls) -> list[Self]:
    #     vals = [
    #         "00011100",
    #         "00101010",
    #         "01001001",
    #         # "01011000",
    #         # "01101000",
    #         # "10001000",
    #         # "10011000",
    #         # "10101000",
    #     ]
    #     batches = []
    #     for val in vals:
    #         state = [bool(int(x)) for x in val]
    #         batches.append(cls(*state))
    #     return batches

    @classmethod
    def _check_value(cls, val: str) -> bool:
        return super()._check_value(val) or val[4] == val[5] == val[6] == val[7] == "1"

    def __str__(self) -> str:
        return "".join([str(int(x)) for x in self])
