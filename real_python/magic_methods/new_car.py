from car_class import Car
import datetime

my_car = Car('red', 24966)

# without magic methods, we just print the memory address
# with __str__ magic method, the string defined in the __str__ method in the class is returned
# use when:  used for easy read representation of a class
print(my_car)
print(str(my_car))

# repr returns the repr for my_car
# use when:  internal use, unambiguous for dev purposes, not to display
print(repr(my_car))

# date example
print('date example')
today = datetime.date.today()
print('str of today is:', str(today))
print('repr of today is:', repr(today),'; and is more verbose than __str__')


