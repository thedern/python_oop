# super is a shortcut to access a 'base' class without having to know the base class's name or type
# to see any classes parent (event base classes parent, which is class 'object', run <instance_name>.__class__.__base__

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


class Cube(Square):
    # same parameters as Square, no need to redefine __init__
    # just needs length to initialize

    def surface_area(self):
        """
        # super NOT called here in the method thus:
        area is looked for in the current object first (self.area), then looks into parent, then grandparent
        :return:
        """
        face_area = self.area()
        return face_area * 6

    def volume(self):
        """
        super called in the method thus:
        area is looked for not in current object first, but Square first, but will still have go up one more level
        to rectangle to find area
        :return:
        """
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'cube!!!'

    def family_tree(self):
        """
        local what_ami_i is called then, parent's, what_am_i
        :return:
        """
        return self.what_am_i() + ' child of ' + super().what_am_i()

