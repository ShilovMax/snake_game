from .base_q_learning_game import BaseQLearningGame
from dataclasses import dataclass
from utils.state import LessOrGreaterState
from players import DeepQLearningPlayer
import torch


@dataclass
class BaseDeepQLearningGame[S: LessOrGreaterState](BaseQLearningGame):
    player: DeepQLearningPlayer
    state: type[S]

    def fake_batch_play(self, sleep: float = 0) -> None:
        states: list[S] = self.state.get_all_possible_states()
        for state in states:
            self._set_playboard_from_state(state=state)
            self.play(endless_win=False, endless_lose=False, sleep=sleep)

    def _learn_batch(self, wins_per_batch_count: int, sleep: float = 0) -> None:
        states: list[S] = self.state.get_all_possible_states()

        for _ in range(wins_per_batch_count):
            for state in states:
                self._set_playboard_from_state(state=state)
                self.play(endless_win=False, endless_lose=True, sleep=sleep)

    def _set_playboard_from_state(self, state: S):
        snake_x, snake_y, apple_x, apple_y = self._get_snake_head_and_apple_from_state(
            state=state
        )
        print(snake_x, snake_y, apple_x, apple_y)
        self.playboard.snake.head.coords = (snake_x, snake_y)
        self.playboard.apple.coords = (apple_x, apple_y)
        return snake_x, snake_y, apple_x, apple_y

    def _save(self, file: str) -> None:
        torch.save(self.player.model.state_dict(), file)

    def _get_state(self) -> LessOrGreaterState:
        return LessOrGreaterState(
            is_head_x_less_than_apple_x=self.snake_head.x < self.apple.x,
            is_head_x_greater_than_apple_x=self.snake_head.x > self.apple.x,
            is_head_y_less_than_apple_y=self.snake_head.y < self.apple.y,
            is_head_y_greater_than_apple_y=self.snake_head.y > self.apple.y,
        )

    def _get_snake_head_and_apple_from_state(self, state: S):
        snake_x, apple_x = 1, 1
        snake_y, apple_y = 1, 1

        if state.is_head_x_less_than_apple_x:
            apple_x = self.playboard.width - 1
        elif state.is_head_x_greater_than_apple_x:
            snake_x = self.playboard.width - 1

        if state.is_head_y_less_than_apple_y:
            apple_y = self.playboard.height - 1
        elif state.is_head_y_greater_than_apple_y:
            snake_y = self.playboard.height - 1

        return snake_x, snake_y, apple_x, apple_y
