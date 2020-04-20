from abc import ABCMeta, abstractmethod

class ItemInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, config):
        pass

    @abstractmethod
    def __dict__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __int__(self):
        pass

    @abstractmethod
    def __json__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __created(self):
        pass
