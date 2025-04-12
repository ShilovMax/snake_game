import pygame as pg
from game import Game

from enum import Enum
from utils.factories import HumanGameFactory, QLearningGameFactory


class GameType(Enum):
    human = HumanGameFactory
    q_learning_game = QLearningGameFactory


pg.init()

game: Game = GameType.q_learning_game.value.create()

game.play()
