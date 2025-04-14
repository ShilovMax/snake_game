from torch import nn

from dataclasses import dataclass


@dataclass
class Layer:
    name: str
    func: nn.Module


class BaseNeuralNetwork(nn.Module):
    def __init__(self, layers: list[Layer]):
        super().__init__()
        self.layers: list[nn.Module] = []
        for layer in layers:
            setattr(
                self,
                layer.name,
                layer.func,
            )
            self.layers.append(getattr(self, layer.name))

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
