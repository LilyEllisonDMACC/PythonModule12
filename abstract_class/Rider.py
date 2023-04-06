"""
Program: Rider.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to create an abstract class for subclasses to abstract methods from.

"""


from abc import ABC, abstractmethod
class Rider(ABC):
    @abstractmethod
    def ride(self):
        raise NotImplementedError("Abstract method not implemented")

    @abstractmethod
    def riders(self):
        raise NotImplementedError("Abstract method not implemented")
