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
# file = MODELS_DIR / "q_matrix.npy"
game.learn(wins_count=100, sleep=0.5)
# game.play(endless=True, sleep=0.5)
