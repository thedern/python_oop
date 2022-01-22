"""
This file defines the productivity system as well as employee roles
"""


class ProductivitySystem:
    """
    productivitySystem's track method calls the 'work' method on each employee roll object
    """

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('\n')


# Roles no longer inherit from employee classes, consist of a single method
# Employees inherit a role from the classes below

class ManagerRole:
    def work(self, hours):
        return f'screams and yells for {hours} hours.'


class SecretaryRole:
    def work(self, hours):
        return f'expends {hours} hours doing paperwork.'


class SalesPersonRole:
    def work(self, hours):
        return f'expends {hours} hours on the phone.'


class FactoryWorkerRole:
    def work(self, hours):
        return f'expends {hours} hours making widgets.'
