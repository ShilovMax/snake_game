from utils.factories import AbstractFactory
from utils.types import TripleInt
from .apple import Apple
from .snake import Snake, SnakeItem
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
    def get_param(cls, param: str) -> int | TripleInt:
        name = f"DEFAULT_{cls.class_to_create.__name__.upper()}_{param}"
        attr = getattr(cf, name)
        if attr is None:
            raise AttributeError(f"Attribute {name} could not be None")
        return attr


class AppleFactory(DrawingObjectFactory):
    class_to_create = Apple


class GridFactory(DrawingObjectFactory):
    class_to_create = Grid


class SnakeItemFactory(DrawingObjectFactory):
    class_to_create = SnakeItem

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs = super(SnakeItemFactory, cls).set_defaults(kwargs=kwargs)
        kwargs.setdefault("is_visible", True)
        return kwargs


class SnakeFactory(AbstractFactory):
    class_to_create = Snake

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("body", [SnakeItemFactory.create()])
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
