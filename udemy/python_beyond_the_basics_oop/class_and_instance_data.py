# instance can access class data and its own data

class InstanceCounter(object):
    # class data counts stores the number of instances
    count = 0

    def __init__(self, val):
        # instance creation takes a value as an argument
        self.val = val
        # update class data with the number of instances
        # count is a global variable, thus needs class.name
        InstanceCounter.count += 1

    def set_val(self, newval):
        # set new value in the instance
        self.val = newval

    def get_val(self):
        # get value from the intance
        return self.val

    def get_count(self):
        # return class data
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    # get instance data
    print(f'val of object is: {obj.get_val()}')
    print(f'count is: {obj.get_count()}')
