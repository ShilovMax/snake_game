from .base_q_learning_game import BaseQLearningGame
from dataclasses import dataclass
from utils.state import LessOrGreaterState
from players import DeepQLearningPlayer
import torch


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

    def _save(self, file: str) -> None:
        torch.save(self.player.model.state_dict(), file)

    @staticmethod
    def get_all_possible_states(pow: int = 4) -> list[LessOrGreaterState]:
        batches: list[LessOrGreaterState] = []
        n: int = 2**pow

        for i in range(n):
            val: str = bin(i)[2:]
            if len(val) < pow:
                val = "0" * (pow - len(val)) + val

            if (
                (val[0] == val[1] == "1")
                or (val[2] == val[3] == "1")
                or (val[0] == val[1] == val[2] == val[3])
            ):
                continue

            state = [bool(int(x)) for x in val]
            batches.append(LessOrGreaterState(*state))

        return batches

    def learn_batches(
        self,
        wins_per_batch_count: int,
        file: str | None = None,
        sleep: float = 0,
    ) -> None:
        self.is_learning = True
        states: list[LessOrGreaterState] = self.get_all_possible_states()

        for _ in range(wins_per_batch_count):
            for state in states:
                self._set_playboard_by_state(state=state)
                self.play(endless=False, sleep=sleep)

        if file:
            self._save(file=file)

        self.is_learning = False

    def fake_batch_play(self, sleep: float = 0):
        states: list[LessOrGreaterState] = self.get_all_possible_states()
        for state in states:
            self._set_playboard_by_state(state=state)
            self.play(endless=False, sleep=sleep)

    def _set_playboard_by_state(self, state: LessOrGreaterState) -> None:
        snake_x, apple_x = 0, 0
        snake_y, apple_y = 0, 0

        if state.is_head_x_less_than_apple_x:
            apple_x = self.playboard.width
        elif state.is_head_x_greater_than_apple_x:
            snake_x = self.playboard.width

        if state.is_head_y_less_than_apple_y:
            apple_y = self.playboard.height
        elif state.is_head_y_greater_than_apple_y:
            snake_y = self.playboard.height

        self.playboard.snake.coords = (snake_x, snake_y)
        self.playboard.apple.coords = (apple_x, apple_y)
