from dataclasses import dataclass

from utils.state import LessOrGreaterState

from .abstract_q_learning_player import AbstractQLearningPlayer
import torch
from torch.optim import Optimizer
from torch.nn.modules.loss import _Loss
from utils.types import Action
from neural_networks import BaseNeuralNetwork
import random


@dataclass
class DeepQLearningPlayer(AbstractQLearningPlayer):
    model: BaseNeuralNetwork
    optimizer: Optimizer
    loss_func: _Loss
    _file: str

    def __post_init__(self) -> None:
        self.file = self._file
        self.second_best_action_probability_per_state = {
            str(x): 0.0
            for x in filter(
                lambda x: sum(x) == 2, LessOrGreaterState.get_all_possible_states()
            )
        }

    @property
    def file(self) -> str:
        return self._file

    @file.setter
    def file(self, val: str) -> None:
        self._file = val
        if self.file:
            self.weights = torch.load(self.file, weights_only=True)
            self.model.load_state_dict(self.weights)
            self.epsilon = 0

    def _get_best_action(self, state: LessOrGreaterState) -> Action:
        q_values = self.model(torch.tensor([*state], dtype=torch.float32))
        vals: list[float] = [round(float(x), 4) for x in q_values]
        result: int = self._get_max(state=state, array=vals)

        return Action(result)

    def _get_max(self, array: list[float], state: LessOrGreaterState) -> int:
        max_index_1: int = array.index(max(array))
        if sum(state) == 2:
            array_copy: list[float] = array.copy()
            array.pop(max_index_1)
            max_value_2: float = max(array)
            max_index_2: int = array_copy.index(max_value_2)
            self.second_best_action_probability_per_state[str(state)] = max_value_2

            return random.choice([max_index_1, max_index_2])

        return max_index_1

    def learn(
        self,
        previous_state: LessOrGreaterState,
        action: Action,
        reward: int,
        current_state: LessOrGreaterState,
    ):
        previous_q_values = self.model(
            torch.tensor([*previous_state], dtype=torch.float32)
        )
        previous_q_value = previous_q_values[action.value]

        current_q_values = self.model(
            torch.tensor([*current_state], dtype=torch.float32)
        )
        max_current_q_value = torch.max(current_q_values)
        target_q_value = reward + self.gamma * max_current_q_value
        loss = self.loss_func(previous_q_value, target_q_value.detach())

        # обновляем веса сети
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
