# polymorphism, both dogs and cats have show_affection methods thus the name interface
# but the show_affection has different behaviors between the dog and cat classes
# an example of polymorphism in python is len(), works on strings, list etc

class Animal(object):
    # top-level class
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} eats{food}')


class Dog(Animal):
    def fetch(self, things):
        print(f'{self.name} goes after {things}')

    def show_affection(self):
        print(f'{self.name} wags tail')


class Cat(Animal):
    def swatstring(self):
        print(f'{self.name} swats the string')

    def show_affection(self):
        print(f'{self.name} purrs loudly')


d = Dog('tiger')
c = Cat('Muffin')

d.fetch('stick')
d.show_affection()

c.swatstring()
c.show_affection()
