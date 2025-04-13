from abc import ABC, abstractmethod
from players import QLearningPlayer
import config as cf
from drawing_objects import Apple, Snake, Grid, TextObject
from game import HumanGame, QLearningGame
from utils.types import ColorType
from surfaces import BasePlayboard, ScoreSurface


class AbstractFactory[C](ABC):
    class_to_create: type[C]

    @classmethod
    def create(cls, **kwargs) -> C:
        kwargs = cls.set_defaults(kwargs)
        return cls.class_to_create(**kwargs)

    @classmethod
    @abstractmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        pass


class DrawingObjectFactory(AbstractFactory):
    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("x", cls.get_param("X"))
        kwargs.setdefault("y", cls.get_param("Y"))
        kwargs.setdefault("color", cls.get_param("COLOR"))
        return kwargs

    @classmethod
    def get_param(cls, param: str) -> int | ColorType:
        name = f"DEFAULT_{cls.class_to_create.__name__.upper()}_{param}"
        attr = getattr(cf, name)
        if attr is None:
            raise AttributeError(f"Attribute {name} could not be None")
        return attr


class AppleFactory(DrawingObjectFactory):
    class_to_create = Apple


class SnakeFactory(DrawingObjectFactory):
    class_to_create = Snake


class GridFactory(DrawingObjectFactory):
    class_to_create = Grid


class QLearningPlayerFactory(AbstractFactory):
    class_to_create = QLearningPlayer

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("learning_rate", cf.LEARNING_RATE)
        kwargs.setdefault("gamma", cf.GAMMA)
        kwargs.setdefault("epsilon", cf.EPSILON)
        kwargs.setdefault("matrix_size", cf.MATRIX_SIZE)
        kwargs.setdefault("file", cf.MATRIX_FILE)
        return kwargs


class BasePlayboardFactory(AbstractFactory):
    class_to_create = BasePlayboard

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("size", cf.PLAYBOARD_SIZE)
        kwargs.setdefault("width", cf.N_WIDTH - 1)
        kwargs.setdefault("height", cf.N_HEIGHT - 1)
        kwargs.setdefault("background_color", cf.PLAYBOARD_BACKGROUND_COLOR)
        kwargs.setdefault("apple", AppleFactory.create())
        kwargs.setdefault("snake", SnakeFactory.create())
        kwargs.setdefault("grid", GridFactory.create())
        return kwargs


class ScoreFactory(AbstractFactory):
    class_to_create = TextObject

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("font_size", cf.SCORE_FONT_SIZE)
        kwargs.setdefault("rect_size", cf.SCORE_TEXT_RECT_SIZE)
        kwargs.setdefault("_text", cf.SCORE_TEXT)
        kwargs.setdefault("color", cf.SCORE_COLOR)
        return kwargs


class ScoreSurfaceFactory(AbstractFactory):
    class_to_create = ScoreSurface

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("score", ScoreFactory.create())
        kwargs.setdefault("size", cf.SCORE_SURFACE_SIZE)
        kwargs.setdefault("background_color", cf.SCORE_BACKGROUND_COLOR)
        return kwargs


class BaseGameFactory(AbstractFactory):
    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("caption", cf.CAPTION)
        kwargs.setdefault("screen_size", cf.SCREEN_SIZE)
        kwargs.setdefault("background_color", cf.BACKGROUND_COLOR)
        kwargs.setdefault("fps", cf.FPS)
        kwargs.setdefault("playboard", BasePlayboardFactory.create())
        kwargs.setdefault("score_surface", ScoreSurfaceFactory.create())
        return kwargs


class HumanGameFactory(BaseGameFactory):
    class_to_create: type[HumanGame] = HumanGame


class QLearningGameFactory(BaseGameFactory):
    class_to_create: type[QLearningGame] = QLearningGame

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs = super().set_defaults(kwargs)
        kwargs.setdefault("player", QLearningPlayerFactory.create())
        return kwargs
