import random


class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        # modular way of inheriting name from the parent
        # calling animal.init fom dog object
        # super gives access to parents methods
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Aussie', 'Swissy', 'Bulldog'])

    def fetch(self, thing):
        print(f'{self.name} goes after a {thing}')


d = Dog('Lego')
print(d.breed)
print(d.name)
