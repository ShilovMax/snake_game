import pygame as pg

from enum import Enum
from config import MODELS_DIR
from utils.factories import HumanGameFactory, QLearningGameFactory


class GameType(Enum):
    human = HumanGameFactory
    q_learning_game = QLearningGameFactory


pg.init()

# game = GameType.human.value.create()
game = GameType.q_learning_game.value.create()
file = MODELS_DIR / "q_matrix.npy"
game.learn(wins_count=100, file=file, sleep=0.5)
# game.play(endless=True, sleep=0.5)
