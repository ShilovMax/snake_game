from abc import ABC, abstractmethod
from dataclasses import dataclass
from utils.types import TripleInt


@dataclass
class AbstractDrawingObject(ABC):
    @abstractmethod
    def draw(self, **kwargs) -> None:
        pass


@dataclass
class ColorMixin:
    color: TripleInt


@dataclass
class XYMixin:
    x: int
    y: int
