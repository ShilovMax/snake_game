from abc import abstractmethod
from dataclasses import dataclass
from game import Game
from players import AbstractQLearningPlayer
from utils.state import BaseState, QLearningState


@dataclass
class BaseQLearningGame[S: BaseState, P: AbstractQLearningPlayer](Game):
    player: P

    def __post_init__(self) -> None:
        super().__post_init__()
        self.is_learning: bool = False

    def _do_updates(self) -> None:
        previous_snake_state = QLearningState(coords=self.playboard.snake.coords)
        previous_state: S = self._get_state()
        self.action = self.player.choose_action(state=previous_state)
        super()._do_updates()

        if self.is_learning:
            self.player.learn(
                previous_state=previous_state,
                action=self.action,
                reward=self._get_reward(previous_state=previous_snake_state),
                current_state=self._get_state(),
            )

    @abstractmethod
    def _get_state(self) -> S:
        raise NotImplementedError

    @abstractmethod
    def _get_reward(self, previous_state: QLearningState) -> int:
        raise NotImplementedError
