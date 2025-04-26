from dataclasses import dataclass
from .base_q_learning_game import BaseQLearningGame
from players import QLearningPlayer
from utils.state import LinearQLearningState, QLearningState
import numpy as np


@dataclass
class QLearningGame(BaseQLearningGame):
    player: QLearningPlayer

    def __post_init__(self) -> None:
        super().__post_init__()
        self.is_learning: bool = False

    def _save(self, file: str) -> None:
        np.save(file, self.player.q_table)

    def _get_state(self) -> QLearningState:
        return LinearQLearningState(
            snake_coords=self.snake_head_coords,
            apple_coords=self.apple_coords,
        ).get_linear_coords(size=self.playboard.width)
