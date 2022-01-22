from dog_class import Dog
from aussie_class import Aussie

# create an Aussie dog named flash
flash = Aussie('Flash', 1)

print(type(flash))

# attributes and methods
print(flash.description)
print(flash.name, flash.age, flash.species)
flash.speak()
flash.bite()
flash.aussie_bite()
flash.birthday()
print(flash.name, flash.age)

# flash is a Dog an Aussie and an object
print(isinstance(flash, Dog))
print(isinstance(flash, Aussie))
print(isinstance(flash, object))
