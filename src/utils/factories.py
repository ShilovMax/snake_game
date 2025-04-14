from abc import ABC, abstractmethod


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
