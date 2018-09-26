from abc import ABCMeta, abstractmethod


class AbstractBaseMediator(metaclass=ABCMeta):

	@abstractmethod
	def run(self):
		pass