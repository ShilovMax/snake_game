from dataclasses import dataclass

from utils.types import CoordsType


@dataclass
class BaseState:
    pass


@dataclass
class QLearningState(BaseState):
    coords: CoordsType
