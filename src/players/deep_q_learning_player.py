from dataclasses import dataclass

from utils.state import LessOrGreaterState

from .abstract_q_learning_player import AbstractQLearningPlayer
import torch
from torch.optim import Optimizer
from torch.nn.modules.loss import _Loss
from utils.types import Action
from neural_networks import BaseNeuralNetwork


@dataclass
class DeepQLearningPlayer(AbstractQLearningPlayer):
    model: BaseNeuralNetwork
    optimizer: Optimizer
    loss_func: _Loss
    _file: str

    def __post_init__(self) -> None:
        self.file = self._file

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
        result = torch.argmax(q_values).item()
        return Action(int(result))

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
