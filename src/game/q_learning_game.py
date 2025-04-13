from dataclasses import dataclass
from .base_q_learning_game import BaseQLearningGame
from players import QLearningPlayer
from utils.state import QLearningState
import numpy as np


@dataclass
class QLearningGame(BaseQLearningGame):
    player: QLearningPlayer

    def learn(self, wins_count: int, file: str | None = None, sleep: float = 0) -> None:
        self.is_learning = True
        while self.score < wins_count:
            self.play(endless=False, sleep=sleep)
        if file:
            np.save(file, self.player.q_table)

        self.is_learning = False

    def _get_state(self) -> QLearningState:
        return QLearningState(coords=self.playboard.snake.coords)

    def _get_reward(self, previous_state: QLearningState) -> int:
        if self._is_eat_apple():
            return 10
        elif self._is_x_distance_decreased(
            previous_state=previous_state
        ) or self._is_y_distance_decreased(previous_state=previous_state):
            return 1
        else:
            return -2

    def _is_eat_apple(self) -> bool:
        return self.playboard.snake.coords == self.playboard.apple.coords

    def _is_x_distance_decreased(self, previous_state: QLearningState) -> bool:
        return (self.playboard.apple.x - previous_state.coords[0]) > (
            self.playboard.apple.y - self.playboard.snake.coords[0]
        )

    def _is_y_distance_decreased(self, previous_state: QLearningState) -> bool:
        return (self.playboard.apple.y - previous_state.coords[1]) > (
            self.playboard.apple.y - self.playboard.snake.coords[1]
        )
