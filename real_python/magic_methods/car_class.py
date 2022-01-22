
class Car:
    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage

    # magic methods __str__ and __repr__
    def __str__(self):
        # returns a string
        return f'a {self.color} car with {self.mileage} miles'

    def __repr__(self):
        """
        Dan Bader recommends always adding a __repr__
        return a string with classname, color, and mileage
        :return: str
        """
        return f'{self.__class__.__name__}({self.color}, {self.mileage})'

