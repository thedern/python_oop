"""
composition:  A class composes an attribute of another class.  This is different than inheritance where a class extends
another class with increased functionality

Tips:  inheritance 'extends' another class
       composition 'implements' another class
"""


class Salary:
    """
    salary class
    calculates annual salary
    """
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    """
    employee class
    calculates annual pay including bonus
    obj_salary is an attribute composed of the Salary class
    """
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        # attribute is an instance of Salary class
        self.total_salary = Salary(self.pay)

    def annual_salary(self):
        return f"Total pay for employee: {str(self.total_salary.get_total() + self.bonus)}"


obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())
