# decorators and static methods are not bound to the instance
# these are unlike instance methods where instance (self) is first argument

# Example
class InstanceCounter(object):
    # class data counts stores the number of instances
    count = 0

    def __init__(self, val):
        # instance creation takes a value as an argument
        # calls static method 'filterint' to check val's type
        self.val = self.filterint(val)
        # update class data with the number of instances
        # count is a global variable, thus needs class.name
        InstanceCounter.count += 1

    def set_val(self, newval):
        # instance method
        # set new value in the instance
        self.val = newval

    def get_val(self):
        # instance method
        # get value from the instance
        return self.val

    @classmethod
    def get_count(cls):
        # class method, passes class as argument ('cls' by convention)
        # net output is the same as if it was an instance method but no longer relies on the instance to execute
        # return class data
        return cls.count

    @staticmethod
    # utility method that is not used by the the instance or class
    # self not passed nor is class, just works with value passed to the class
    # used as a guardian function against crap passed into init (see init at top)
    def filterint(value):
        if not isinstance(value, int):
            # if not integer, return 0 to calling function
            return 0
        else:
            return value


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('dog')

print(a.val)
print(b.val)
print(c.val)
