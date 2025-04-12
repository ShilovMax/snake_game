from dataclasses import dataclass


@dataclass
class BaseState:
    pass


@dataclass
class QLearningState(BaseState):
    coords: tuple[int, int]
