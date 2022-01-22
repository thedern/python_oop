# Abstract classes define blueprints for other classes to be defined
# not intended to be used ot create instances itself, but used by other classes to create instances
# Used to define interfaces or methods other class must use

# NON WORKING EXAMPLE

import abc


class GetterSetter(object):
    __metaclass__ = abc

    @abc.abstractmethod
    def set_val(self, input):
        """set a value in the instance"""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get and return value from the instance of the class"""
        return
