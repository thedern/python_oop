# class attributes apply to all instances of a class
# instance attribute apply to only a specific instance of a class

class MyClass(object):
    # class_at belongs to the class is is present in all instances of the class
    class_at = 100

    # instance at is only set when an instance of the class has the set_val method invoked
    def set_val(self):
        self.instance_at = 1


# create instance and print class attribute
a = MyClass()
print(a.class_at)
# the code below will generate an AttributeError as set_val was not called
# print(a.instance_at)

# create instance and print class and instance attribute
b = MyClass()
print(b.class_at)
# create a new attribute that only exits in instance 'b'
b.set_val()
print(b.instance_at)

