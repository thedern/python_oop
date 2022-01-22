# encapsulation
# setting values via instance methods to ensure data integrity vs setting values on the instance directly

class MyClass(object):
    # class includes getter and setter functions

    # set value passed to the method as value
    def set_val(self, val):
        # guardian statement ensures that val is an integer
        try:
            val = int(val)
        except ValueError:
            return
        self.int_value = val

    # get the value of 'value' variable
    def get_val(self):
        return self.int_value


# create instances of MyClass
a = MyClass()
b = MyClass()

# execute setter class method
a.set_val(10)
b.set_val(100)

# execute getter class method
print(a.get_val())
print(b.get_val())

# setting values directly on the instance would work and could also bypass the integrity check
b.int_value = 'cat'
print(b.get_val())