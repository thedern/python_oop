from hr import SalaryPolicy, CommissionPolicy, HourlyPolicy
from productivity import ManagerRole, SecretaryRole, SalesPersonRole, FactoryWorkerRole


class Employee:
    # base class
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Multiple Inheritance Below
# Employees inherit all attributes and methods from other classes
# Attributes and Methods inherited are from a linear tree where inheriting identical attributes and methods from more
# than one class is reduced or avoided.  For instance, SalaryPo
# This pattern helps avoid the diamond problem


class Manager(Employee, ManagerRole, SalaryPolicy):
    # create init that contains required args
    def __init__(self, id, name, weekly_salary):
        # init from SalaryPolicy to get access to weekly_salary attribute
        SalaryPolicy.__init__(self, weekly_salary)
        # get id, name attributes from Employee
        super().__init__(id, name)
        # ManagerRole has no attributes, just a single method, no specific init needed


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    # create init that contains required args
    def __init__(self, id, name, weekly_salary):
        # init from SalaryPolicy to get access to weekly_salary attributes
        SalaryPolicy.__init__(self, weekly_salary)
        # get id, name attributes from Employee
        super().__init__(id, name)
        # SecretaryRole has no instance attributes, just a single method, no specific init needed


class FactoryWorker(Employee, FactoryWorkerRole, HourlyPolicy):
    # create init that contains required args
    def __init__(self, id, name, hours_worked, hour_rate):
        # init from HourlyPolicy to get access to hours_worked, hour_rate attributes
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        # get id, name attributes from Employee
        super().__init__(id, name)
        # FactoryWorkerRole has no instance attributes, just a single method, no specific init needed


class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    # create init that contains required args
    def __init__(self, id, name, hours_worked, hour_rate):
        # init from HourlyPolicy to get access to hours_worked, hour_rate attributes
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        # get id, name attributes from Employee
        super().__init__(id, name)
        # SecretaryRole has no instance attributes, just a single method, no specific init needed


class SalesPerson(Employee, SalesPersonRole, CommissionPolicy):
    # create init that contains required args
    def __init__(self, id, name, weekly_salary, commission):
        # init from CommissionPolicy to get access to hours_worked, hour_rate attributes
        CommissionPolicy.__init__(self, weekly_salary, commission)
        # get id, name attributes from Employee
        super().__init__(id, name)
        # SalesPersonRole has no instance attributes, just a single method, no specific init needed

