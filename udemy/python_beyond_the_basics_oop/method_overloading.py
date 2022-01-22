

import abc


# abstract parent class
# cannot be instantiated directly but is used by other classes
class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    # abstract method which does not do anything aside from creating method blueprint
    @abc.abstractmethod
    def showdoc(self):
        return


# child class inherits from parent
# uses only 2 methods from parent
class GetSetInt(GetSetParent):

    """
    instance's set val will check the value type is an int
    then, it calls set_val from parent to actually set the value
    """

    def set_val(self, value):
        # check type, override/overload he parents' method
        if not isinstance(value, int):
            value = 0
        # call set val from parent
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print('GetSetInt object ({0}), only accepts integer values'.format(id(self)))


# child class inherits from parent
class GetSetList(GetSetParent):
    # instantiate a list with an initial value, default is 0
    def __init__(self, value=0):
        self.vallist = [value]

    # returns the last value in the list
    def get_val(self):
        return self.vallist[-1]

    # returns list
    def get_vals(self):
        return self.vallist

    # append to list
    # polymorphic set_val where instance has its own version seperate of parent's
    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print('GetSetList object, len {0} stores history of values set'.format(len(self.vallist)))

# create list and set initial value
gsl = GetSetList()

# append to list
gsl.set_val(10)
gsl.set_val(20)

# get the last value in the list
print(gsl.get_val())

# get the whole list
print(gsl.get_vals())

# show the print statement
gsl.showdoc()


gsi = GetSetInt('cat')
gsi.showdoc()
