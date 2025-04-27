from .playboards import BasePlayboard, LongSnakePlayboard
from .metrics import ScoreSurface
from utils.factories import AbstractFactory
import config as cf
from drawing_objects.factories import (
    AppleFactory,
    SnakeFactory,
    GridFactory,
    ScoreFactory,
)


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


class LongSnakePlayboardFactory(BasePlayboardFactory):
    class_to_create = LongSnakePlayboard


class ScoreSurfaceFactory(AbstractFactory):
    class_to_create = ScoreSurface

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("score", ScoreFactory.create())
        kwargs.setdefault("size", cf.SCORE_SURFACE_SIZE)
        kwargs.setdefault("background_color", cf.SCORE_BACKGROUND_COLOR)
        return kwargs
