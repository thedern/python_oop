class Circle():
    def __init__(self, x=1):
        self.x = x

    def radius(self):
        return self.x

    def diameter(self):
        return self.x * 2

    def area(self):
        return (3.15 * self.x) ** 2
