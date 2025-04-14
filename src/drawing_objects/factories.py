from utils.factories import AbstractFactory
from utils.types import ColorType
from .apple import Apple
from .snake import Snake
from .grid import Grid
from .text import TextObject
import config as cf


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


class ScoreFactory(AbstractFactory):
    class_to_create = TextObject

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("font_size", cf.SCORE_FONT_SIZE)
        kwargs.setdefault("rect_size", cf.SCORE_TEXT_RECT_SIZE)
        kwargs.setdefault("_text", cf.SCORE_TEXT)
        kwargs.setdefault("color", cf.SCORE_COLOR)
        return kwargs
