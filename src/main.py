import pygame as pg

from enum import Enum
from config import MODELS_DIR
from game.factories import (
    HumanGameFactory,
    LongSnakeDeepQLeatningGameFactory,
    QLearningGameFactory,
    DeepQLearningGameFactory,
)
from utils.state import PlusShapedVisionLessOrGreateStateState


class GameType(Enum):
    human = HumanGameFactory
    q_learning_game = QLearningGameFactory
    deep_q_learning_game = DeepQLearningGameFactory
    long_snake_deep_q_learning_game = LongSnakeDeepQLeatningGameFactory


pg.init()

states = PlusShapedVisionLessOrGreateStateState.get_all_possible_states()
print(len(states))

# game = GameType.long_snake_deep_q_learning_game.value.create(long=True)
# import time

# for state in states:
#     game._set_playboard_from_state(state=state)
#     game._draw()
#     time.sleep(2)

# raise

game = GameType.human.value.create(long=True)
game.play(endless_win=True, endless_lose=False)
raise
# game = GameType.deep_q_learning_game.value.create()
game = GameType.long_snake_deep_q_learning_game.value.create(long=True)
file0 = MODELS_DIR / "model_v2.pth"
file1 = MODELS_DIR / "model_v2_batch.pth"
file2 = MODELS_DIR / "model_v2_batch_till_high_probability_46.pth"
file3 = MODELS_DIR / "model_v2_batch_till_high_probability_40.pth"
file4 = MODELS_DIR / "model_v3.pth"

# game.learn(
#     #     # mode=LearnMode.till_wins_count,
#     #     # wins_count=100,
#     mode=LearnMode.batch,
#     wins_per_batch_count=50,
#     #     # mode=LearnMode.till_high_probability_of_second_best_action,
#     #     # probability=0.3,
#     file=file4,
#     #     # sleep=0.5,
# )
game.player.epsilon = 0
game.player.file = file4
# game.fake_batch_play(sleep=1)

scores = []
for i in range(100):
    game.play(endless_win=True, endless_lose=False)
    # time.sleep(5)
    game.snake.body = game.snake.body[:1]
    scores.append(game.score)
    game.score = 0
    game.playboard.reset_apple(is_random=True)
# import time
print(max(scores), sum(scores) / 100, min(scores))
print(sorted(scores))
# time.sleep(1)

# 10001110
# q values [0.0007, 0.5537, 0.0, 0.4456]
