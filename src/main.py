import pygame as pg

from enum import Enum
from config import MODELS_DIR
from game.factories import (
    HumanGameFactory,
    QLearningGameFactory,
    DeepQLearningGameFactory,
)


class GameType(Enum):
    human = HumanGameFactory
    q_learning_game = QLearningGameFactory
    deep_q_learning_game = DeepQLearningGameFactory


pg.init()

# game = GameType.human.value.create()
game = GameType.deep_q_learning_game.value.create()
file0 = MODELS_DIR / "model_v2.pth"
file1 = MODELS_DIR / "model_v2_batch.pth"
# game.learn(
#     wins_count=300,
#     # sleep=0.5,
#     file=file,
# )
# game.learn_batches(wins_per_batch_count=100, file=file1)
game.player.epsilon = 0
game.player.file = file1
game.fake_batch_play(sleep=0.5)
