from abc import ABC, abstractmethod
from dataclasses import dataclass
from utils.types import ColorType


@dataclass
class AbstractDrawingObject(ABC):
    color: ColorType

    @abstractmethod
    def draw(self, **kwargs) -> None:
        pass


@dataclass
class AbstractXYObject(AbstractDrawingObject):
    x: int
    y: int
