from utils.factories import AbstractFactory
import config as cf
from .human_game import HumanGame
from .q_learning_game import QLearningGame
from .deep_q_learning_game import DeepQLearningGame
from .long_snake_deep_q_learning_game import LongSnakeDeepQLearningGame
from surfaces.factories import (
    BasePlayboardFactory,
    ScoreSurfaceFactory,
    LongSnakePlayboardFactory,
)
from players.factories import QLearningPlayerFactory, DeepQLearningPlayerFactory


class BaseGameFactory(AbstractFactory):
    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("caption", cf.CAPTION)
        kwargs.setdefault("screen_size", cf.SCREEN_SIZE)
        kwargs.setdefault("background_color", cf.BACKGROUND_COLOR)
        kwargs.setdefault("fps", cf.FPS)

        if kwargs.pop("long", False):
            kwargs.setdefault("playboard", LongSnakePlayboardFactory.create())
        else:
            kwargs.setdefault("playboard", BasePlayboardFactory.create())

        kwargs.setdefault("score_surface", ScoreSurfaceFactory.create())
        return kwargs


class HumanGameFactory(BaseGameFactory):
    class_to_create = HumanGame


class QLearningGameFactory(BaseGameFactory):
    class_to_create = QLearningGame

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs = super().set_defaults(kwargs)
        kwargs.setdefault("player", QLearningPlayerFactory.create())
        return kwargs


class DeepQLearningGameFactory(BaseGameFactory):
    class_to_create = DeepQLearningGame

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs = super().set_defaults(kwargs)
        kwargs.setdefault("player", DeepQLearningPlayerFactory.create())
        return kwargs


class LongSnakeDeepQLeatningGameFactory(DeepQLearningGameFactory):
    class_to_create = LongSnakeDeepQLearningGame
