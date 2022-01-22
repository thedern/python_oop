from abc import ABC, abstractmethod

# Employee Base and Derived Classes


class Employee(ABC):
    """
    Base class for other employee type
    This is an Abstract Class.
    # Abstract classes exist to be inherited from and NOT instantiated directly #
    Employee is missing a calculate_payroll classmethod thus will error if we instantiate directly in program.py
    implementing Employee as a child of ABC is OPTIONAL, code will work without it.  This is self documenting code only
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    # adding abstract method will tell other developers this is class to be inherited from only
    # tells code that children that they need to implement their own calculate_payroll
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    """
    # extends base Employee
    # SalaryEmployee also requires id and name as well as new attribute, weekly_salary
    # we need an init but it overrides base Employee's init with own id and name
    # after init we call super's init (parent) so we can use that name and id, not being redundant with our attributes
    """

    def __init__(self, id, name, weekly_salary):
        # re-init base so any SalaryEmployee can be used as a base Employee and have access to base Employee attributes
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        """
        :return: weekly salary attribute
        :rtype: float
        """
        return self.weekly_salary


class HourlyEmployee(Employee):
    """
    see notes above.  Same rational for Hourly employee as Salary Employee
    """

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    """
    extends SalaryEmployee as its base class (parent)
    """

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_commission(self):
        # execute parent's calculate_payroll method.   If the parent changes the CommissionEmployee will too
        fixed_salary = super().calculate_payroll()
        return self.commission + fixed_salary


# EMPLOYEE ROLES


class Manager(SalaryEmployee):
    #  we do not need to declare init explicitly, it will use init from parent, SalaryEmployee
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


class Secretary(SalaryEmployee):
    #  we do not need to declare init explicitly, it will use init from parent, SalaryEmployee
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing paperwork.')


class SalesPerson(CommissionEmployee):
    #  we do not need to declare init explicitly, it will use init from parent, CommissionEmployee
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


class FactoryWorker(HourlyEmployee):
    #  we do not need to declare init explicitly, it will use init from parent, HourlyEmployee
    def work(self, hours):
        print(f'{self.name} expends {hours} hours making widgets.')


# Multiple Inheritance Example "COMPLEX SO STUDY THIS MORE!!!"
class TemporarySecretary(Secretary, HourlyEmployee):
    # init methods are checked in order, Method Resolution Order (MRO)
    # need to override the Secretary and HourlyEmployee init methods with our own to avoid MRO errors when instantiate
    def __init__(self, id, name, hours_worked, hour_rate):

        # cannot use super().__init__ due to having TWO parents, need to pick ONE
        # TemporarySecretary needs to extend HourlyEmployee in order to calculate pay by the hour vs the week
        # we only want the 'work' method from the Secretary class

        # it hits the 'work' method of Secretary first, before the 'work' method of HourlyEmployee (see import order),
        # so it returns that one first and we are good to go there.

        # we call payroll on HourlyEmployee directly due to its conforming with the arguments in our init

        # this design introduces the "DIAMOND PROBLEM", there is a better way to design

        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)
