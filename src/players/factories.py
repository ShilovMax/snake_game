from .q_learning_player import QLearningPlayer
from .deep_q_learning_player import DeepQLearningPlayer
from utils.factories import AbstractFactory
import config as cf
from neural_networks.factories import BaseNeuralNetworkFactory


class QLearningPlayerFactory(AbstractFactory):
    class_to_create = QLearningPlayer

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("learning_rate", cf.LEARNING_RATE)
        kwargs.setdefault("gamma", cf.GAMMA)
        kwargs.setdefault("epsilon", cf.EPSILON)
        kwargs.setdefault("min_epsilon", cf.MIN_EPSILON)
        kwargs.setdefault("epsilon_decay", cf.EPSILON_DECAY)
        kwargs.setdefault("matrix_size", cf.MATRIX_SIZE)
        kwargs.setdefault("file", cf.MATRIX_FILE)
        return kwargs


class DeepQLearningPlayerFactory(AbstractFactory):
    class_to_create = DeepQLearningPlayer

    @classmethod
    def set_defaults(cls, kwargs: dict) -> dict:
        kwargs.setdefault("gamma", cf.GAMMA)
        kwargs.setdefault("epsilon", cf.EPSILON)
        kwargs.setdefault("model", BaseNeuralNetworkFactory.create())
        kwargs.setdefault("optimizer", cf.OPTIMIZER(kwargs["model"].parameters()))
        kwargs.setdefault("loss_func", cf.LOSS_FUNC)
        kwargs.setdefault("_file", cf.TORCH_FILE)
        return kwargs
