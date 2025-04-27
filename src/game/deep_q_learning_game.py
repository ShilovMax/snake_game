from dataclasses import dataclass, field
from utils.state import LessOrGreaterState
from .base_deep_q_learning_game import BaseDeepQLearningGame


@dataclass
class DeepQLearningGame(BaseDeepQLearningGame):
    state: type[LessOrGreaterState] = field(init=False, default=LessOrGreaterState)

    def _learn_till_high_probability_of_second_best_action(
        self,
        probability: float,
        sleep: float = 0,
    ):
        states: list[LessOrGreaterState] = LessOrGreaterState.get_all_possible_states()

        while not all(
            x > probability
            for x in self.player.second_best_action_probability_per_state.values()
        ):
            for state in states:
                self._set_playboard_from_state(state=state)
                self.play(endless_win=False, endless_lose=True, sleep=sleep)
