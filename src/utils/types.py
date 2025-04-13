from enum import Enum

ColorType = tuple[int, int, int]
CoordsType = tuple[int, int]


class Action(Enum):
    left = 0
    right = 1
    up = 2
    down = 3
    stay = 4
