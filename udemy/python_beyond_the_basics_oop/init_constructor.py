# the init constructor is used to initialize attributes on an instance as soon
# as the instance is created and NOT only when specific methods are called

class MyClass(object):
    # initialize the int_val as 10 once the instance is created
    # dunder init __init__ is a private method
    def __init__(self):
        # initial val set to 10 on instance creation
        self.int_val = 10

    # increment instance
    # int_val defaults to 2 if no argument is passed
    def increment_val(self, int_val=2):
        self.int_val += int_val
        print(self.int_val)


# create instance of MyClass
a = MyClass()

# call instance method
a.increment_val()

# call instance method with argument
a.increment_val(10)

