
class Rectangle:
    """
    Rectangle is the base class of both Square and Cube
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def what_am_i(self):
        return 'rectangle!!!'


class Square(Rectangle):
    """
    Square inherits from rectangle and has access to rectangle's methods.
    Square, all sides are equal thus just needs length.  Square's __init__ overrides Rectangle's __init__
    super().__init__ Passes in length twice to parents __init__ so it can use Rectangles methods that require 2 arguments
    """
    def __init__(self, length):
        # calls parent's __init__ after its own
        super().__init__(length, length)

    # via super, calls parent's what_am_i() and not its own
    def what_am_i_a_child_of(self):
        return super().what_am_i()

    def what_am_i(self):
        return "square!!!"


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return "triangle"


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return "right pyramid"

