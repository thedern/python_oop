# one class may inherit from another class

class Car(object):
    # car inherits from object
    def __init__(self):
        self.wheels = 4
        self.left_hand_drive = True


class Jeep(Car):
    # jeep inherits from car
    four_wheel_drive = True
    convertible = True

    def get_attributes(self):
        print(f'wheels: {self.wheels}\nlef-hand-drive: {self.left_hand_drive}\nfour-wheel-drive: {self.four_wheel_drive}\nconvertible: {self.convertible}')


j = Jeep()
j.get_attributes()
