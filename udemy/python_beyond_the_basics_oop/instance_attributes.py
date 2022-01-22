# Instance attributes 'state'
# note this is kinda crappy code :)
import random


class MyClass(object):
    # instance method which sets an instance attribute
    def class_method_one(self):
        # self is required, the first arg passed to a method is the instance of the class
        self.rand_val = random.randint(1, 100)


# create class instance
x = MyClass()

# execute class method which populates the instance attribute, rand_val
x.class_method_one()

# print rand val
print(x.rand_val)
