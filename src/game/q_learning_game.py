from dataclasses import dataclass
from .base_q_learning_game import BaseQLearningGame
from players import QLearningPlayer
from state import QLearningState


@dataclass
class QLearningGame(BaseQLearningGame):
    player: QLearningPlayer

    def _get_state(self) -> QLearningState:
        return QLearningState(coords=self.snake.coords)

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
        return self.snake.coords == self.apple.coords

    def _is_x_distance_decreased(self, previous_state: QLearningState) -> bool:
        return (self.apple.coords[0] - previous_state.coords[0]) > (
            self.apple.coords[0] - self.snake.coords[0]
        )

    def _is_y_distance_decreased(self, previous_state: QLearningState) -> bool:
        return (self.apple.coords[1] - previous_state.coords[1]) > (
            self.apple.coords[1] - self.snake.coords[1]
        )
