from abc import ABC, abstractmethod
from dataclasses import dataclass
from utils.state import BaseState
from utils.types import Action
import random


@dataclass
class AbstractQLearningPlayer[S: BaseState](ABC):
    gamma: float
    epsilon: float

    @abstractmethod
    def learn(
        self,
        previous_state: S,
        reward: int,
        current_state: S,
        action: Action,
    ) -> None:
        raise NotImplementedError

    def choose_action(self, state: S) -> Action:
        if action := self._get_random_action():
            return action
        return self._get_best_action(state=state)

    def _get_random_action(self) -> Action | None:
        if random.uniform(0, 1) < self.epsilon:
            int_action: int = random.randint(0, 3)
            return Action(int_action)

    @abstractmethod
    def _get_best_action(self, state: S) -> Action:
        pass
