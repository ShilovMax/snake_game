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
        self._rewards: dict = {
            self._is_eat_apple: 10,
            self._is_x_distance_decreased: 1,
            self._is_y_distance_decreased: 1,
        }

    @property
    def snake_coords(self) -> tuple[int, int]:
        return self.playboard.snake.coords

    @property
    def apple_coords(self) -> tuple[int, int]:
        return self.playboard.apple.coords

    def learn(self, wins_count: int, file: str | None = None, sleep: float = 0) -> None:
        self.is_learning = True
        while self.score < wins_count:
            self.play(endless=False, sleep=sleep)
        if file:
            self._save(file=file)

        self.is_learning = False

    def _do_updates(self) -> None:
        if not self.is_learning:
            return super()._do_updates()

        previous_snake_state = QLearningState(coords=self.playboard.snake.coords)
        previous_state: S = self._get_state()
        self.action = self.player.choose_action(state=previous_state)
        super()._do_updates()

        self.player.learn(
            previous_state=previous_state,
            action=self.action,
            reward=self._get_reward(previous_state=previous_snake_state),
            current_state=self._get_state(),
        )

    def _get_reward(self, previous_state: QLearningState) -> int:
        for func in self._rewards:
            if func(previous_state=previous_state):
                return self._rewards[func]
        return -2

    def _is_eat_apple(self, **kwargs) -> bool:
        return self.playboard.snake.coords == self.playboard.apple.coords

    def _is_x_distance_decreased(self, previous_state: QLearningState) -> bool:
        return abs(self.playboard.apple.x - previous_state.coords[0]) > abs(
            self.playboard.apple.x - self.playboard.snake.coords[0]
        )

    def _is_y_distance_decreased(self, previous_state: QLearningState) -> bool:
        return abs(self.playboard.apple.y - previous_state.coords[1]) > abs(
            self.playboard.apple.y - self.playboard.snake.coords[1]
        )

    @abstractmethod
    def _save(self, file: str) -> None:
        raise NotADirectoryError

    @abstractmethod
    def _get_state(self) -> S:
        raise NotImplementedError
