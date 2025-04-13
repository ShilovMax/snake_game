from dataclasses import dataclass
from .abstract_q_learning_player import AbstractQLearningPlayer

import numpy as np
import random
from utils.types import Action
from utils.state import QLearningState


@dataclass
class QLearningPlayer(AbstractQLearningPlayer):
    matrix_size: tuple[int, int, int]
    file: str

    def __post_init__(self):
        if self.file:
            self.q_table = np.load(self.file)
            self.epsilon = 0
        else:
            self.q_table: np.ndarray = np.zeros(self.matrix_size)

    def choose_action(self, state: QLearningState) -> Action:
        if random.uniform(0, 1) < self.epsilon:
            int_action: int = random.randint(0, 3)
            return Action(int_action)
        action: Action = self._get_best_action(state=state)
        return action

    def learn(
        self,
        previous_state: QLearningState,
        reward: int,
        current_state: QLearningState,
        action: Action,
    ) -> None:
        best_current_action: Action = self._get_best_action(state=current_state)
        current_step_potential_reward: float = self._get_current_step_potential_reward(
            position=current_state.coords + (best_current_action.value,)
        )

        previous_position: tuple[int, int, int] = previous_state.coords + (
            action.value,
        )

        q_target: float = reward + current_step_potential_reward
        q_delta: float = float(q_target - self._get_q(position=previous_position))

        self._set_q(position=previous_position, value=self.learning_rate * q_delta)

    def _get_best_action(self, state: QLearningState) -> Action:
        array: list[float] = [float(x) for x in self._get_q(position=state.coords)]
        r = self._get_max(array=array)
        return r

    def _get_q(self, position: tuple) -> np.ndarray:
        return self.q_table[position]

    def _set_q(self, position: tuple, value: float) -> None:
        self.q_table[position] += value

    def _get_current_step_potential_reward(self, position: tuple) -> float:
        """
        Возвращает максимальную награду, которую можно получить на текущем шаге * гамма
        """
        return float(self.gamma * self._get_q(position=position))

    def _get_max(self, array: list[float]) -> Action:
        mx: float = max(array)
        if array.count(mx) > 1:
            indecies: list[int] = []
            for num, el in enumerate(array):
                if el == mx:
                    indecies.append(num)
            choice: int = random.choice(indecies)
            return Action(choice)
        return Action(array.index(mx))
