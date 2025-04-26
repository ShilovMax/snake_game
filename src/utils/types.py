from enum import Enum

TripleInt = tuple[int, int, int]
DoubleInt = tuple[int, int]


class Action(Enum):
    left = 0
    right = 1
    up = 2
    down = 3
    stay = 4


class LearnMode(Enum):
    till_wins_count = "till_wins_count"
    batch = "batch"
    till_high_probability_of_second_best_action = (
        "till_high_probability_of_second_best_action"
    )
