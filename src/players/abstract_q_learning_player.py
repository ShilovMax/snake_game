from abc import ABC, abstractmethod
from dataclasses import dataclass
from utils.action import Action


@dataclass
class AbstractQLearningPlayer[S](ABC):
    learning_rate: float
    gamma: float
    epsilon: float

    @abstractmethod
    def choose_action(self, state: S) -> Action:
        raise NotImplementedError

    @abstractmethod
    def learn(
        self,
        previous_state: S,
        reward: int,
        current_state: S,
        action: Action,
    ) -> None:
        raise NotImplementedError
