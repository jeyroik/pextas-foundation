from abc import ABC, abstractmethod

class ItemInterface(ABC):

    @abstractmethod
    def __init__(self, config):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __int__(self):
        pass

    @abstractmethod
    def json_encode(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def created(self):
        pass
