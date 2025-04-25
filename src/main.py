import pygame as pg

from enum import Enum
from config import MODELS_DIR
from game.factories import (
    HumanGameFactory,
    QLearningGameFactory,
    DeepQLearningGameFactory,
)
from utils.types import LearnMode


class GameType(Enum):
    human = HumanGameFactory
    q_learning_game = QLearningGameFactory
    deep_q_learning_game = DeepQLearningGameFactory


pg.init()

# game = GameType.human.value.create()
game = GameType.deep_q_learning_game.value.create()
file0 = MODELS_DIR / "model_v2.pth"
file1 = MODELS_DIR / "model_v2_batch.pth"
file2 = MODELS_DIR / "model_v2_batch_till_high_probability_46.pth"
file3 = MODELS_DIR / "model_v2_batch_till_high_probability_40.pth"

game.learn(
    # mode=LearnMode.till_wins_count,
    # wins_count=100,
    # mode=LearnMode.batch,
    # wins_per_batch_count=5,
    mode=LearnMode.till_high_probability_of_second_best_action,
    probability=0.4,
    # file=file4,
    # sleep=0.05,
)
# game.player.epsilon = 0
# game.player.file = file4
# game.fake_batch_play(sleep=0.2)
