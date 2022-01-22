# Basic class that has 2 variables and one method

class MyClass(object):
    var = 10
    var2 = 20

    # instance method
    def class_method_one(self):
        # self is required, the first arg passed to a method is the instance of the class
        print('hello world')
        print('self is', self)


# instance of MyClass
x = MyClass()
print(x.var)

# second instance of MyClass
y = MyClass()
print(y.var2)
y.class_method_one()

# proof that the instance passed to the method is the same instance we created in 'y'
print('y is', y)
