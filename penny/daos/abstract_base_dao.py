from abc import ABCMeta, abstractmethod


class AbstractBaseDAO(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create(obj):
        pass

    @staticmethod
    @abstractmethod
    def read(id):
        pass

    @staticmethod
    @abstractmethod
    def update(obj):
        pass

    @staticmethod
    @abstractmethod
    def delete(id):
        pass

    @staticmethod
    @abstractmethod
    def list():
        pass
