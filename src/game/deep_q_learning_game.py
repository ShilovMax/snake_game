from .base_q_learning_game import BaseQLearningGame
from dataclasses import dataclass
from utils.state import LessOrGreaterState
from players import DeepQLearningPlayer


@dataclass
class DeepQLearningGame(BaseQLearningGame):
    player: DeepQLearningPlayer

    def _get_state(self) -> LessOrGreaterState:
        return LessOrGreaterState(
            is_head_x_less_than_apple_x=self.snake_coords[0] < self.apple_coords[0],
            is_head_x_greater_than_apple_x=self.snake_coords[0] > self.apple_coords[0],
            is_head_y_less_than_apple_y=self.snake_coords[1] < self.apple_coords[1],
            is_head_y_greater_than_apple_y=self.snake_coords[1] > self.apple_coords[1],
        )
