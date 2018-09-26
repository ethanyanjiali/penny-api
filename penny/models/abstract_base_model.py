from abc import ABCMeta, abstractmethod

class AbstractBaseModel(metaclass=ABCMeta):

	@classmethod
	@abstractmethod
	def from_dict(cls, obj):
		pass

	@abstractmethod
	def to_dict(self):
		pass