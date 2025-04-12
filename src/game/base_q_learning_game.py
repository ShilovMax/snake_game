from abc import abstractmethod
from dataclasses import dataclass
from game import Game
from players import AbstractQLearningPlayer


@dataclass
class BaseQLearningGame[S, P: AbstractQLearningPlayer](Game):
    player: P

    def _do_updates(self) -> None:
        previous_state: S = self._get_state()
        self.action = self.player.choose_action(state=previous_state)
        super()._do_updates()

        self.player.learn(
            previous_state=previous_state,
            action=self.action,
            reward=self._get_reward(previous_state=previous_state),
            current_state=self._get_state(),
        )

    @abstractmethod
    def _get_state(self) -> S:
        raise NotImplementedError

    @abstractmethod
    def _get_reward(self, previous_state: S) -> int:
        raise NotImplementedError
