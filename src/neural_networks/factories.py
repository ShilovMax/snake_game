from utils.factories import AbstractFactory
from .base import BaseNeuralNetwork, Layer
import config as cf


class LayerFactory(AbstractFactory):
    class_to_create = Layer

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        return kwargs


class BaseNeuralNetworkFactory(AbstractFactory):
    class_to_create = BaseNeuralNetwork

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("layers", [LayerFactory.create(**x) for x in cf.NN_LAYERS])
        return kwargs
