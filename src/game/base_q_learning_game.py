from abc import abstractmethod
from dataclasses import dataclass
from game import Game
from players import AbstractQLearningPlayer
from utils.state import BaseState, QLearningState
from utils.types import LearnMode


@dataclass
class BaseQLearningGame[S: BaseState, P: AbstractQLearningPlayer](Game):
    player: P

    def __post_init__(self) -> None:
        super().__post_init__()
        self.is_learning: bool = False
        self._rewards: dict = {
            self._is_out_of_playboard: -10,
            self._is_damage_itself: -10,
            self._is_eat_apple: 10,
            self._is_x_distance_decreased: 1,
            self._is_y_distance_decreased: 1,
        }
        self.learn_funcs = {
            LearnMode.till_wins_count: self._learn_till_wins_count,
            LearnMode.batch: self._learn_batch,
            LearnMode.till_high_probability_of_second_best_action: self._learn_till_high_probability_of_second_best_action,
        }

    def learn(self, mode: LearnMode, file: str | None = None, **kwargs) -> None:
        self.is_learning = True
        self.learn_funcs[mode](**kwargs)
        if file:
            self._save(file=file)

        self.is_learning = False

    def _learn_till_wins_count(self, wins_count: int, sleep: float = 0) -> None:
        while self.score < wins_count:
            self.play(endless_win=False, endless_lose=True, sleep=sleep)

    def _learn_batch(self, **kwargs) -> None:
        pass

    def _learn_till_high_probability_of_second_best_action(self, **kwargs) -> None:
        pass

    def _do_updates(self) -> None:
        previous_snake_state = QLearningState(coords=self.playboard.snake.head.coords)
        previous_state: S = self._get_state()
        self.action = self.player.choose_action(state=previous_state)
        super()._do_updates()
        if not self.is_learning:
            return
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
        return self.playboard.snake.coords[0] == self.playboard.apple.coords

    def _is_x_distance_decreased(self, previous_state: QLearningState) -> bool:
        return abs(self.playboard.apple.x - previous_state.coords[0]) > abs(
            self.playboard.apple.x - self.playboard.snake.head.x
        )

    def _is_y_distance_decreased(self, previous_state: QLearningState) -> bool:
        return abs(self.playboard.apple.y - previous_state.coords[1]) > abs(
            self.playboard.apple.y - self.playboard.snake.head.y
        )

    def _is_out_of_playboard(self, **kwargs) -> bool:
        return any([
            self.snake.head.x < 0,
            self.snake.head.x > self.playboard.width,
            self.snake.head.y < 0,
            self.snake.head.y > self.playboard.height,
        ])

    def _is_damage_itself(self, **kwargs) -> bool:
        return (
            self.playboard.previous_snake_coords == self.snake.coords[::-1]
            or self.snake.head.coords in self.snake.body_visible_coords
        )

    @abstractmethod
    def _save(self, file: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def _get_state(self) -> S:
        raise NotImplementedError
