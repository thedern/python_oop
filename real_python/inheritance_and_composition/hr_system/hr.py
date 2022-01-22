
# Payroll System Classes

class PayrollSystem:
    """
    PayrollSystem's calculate_payroll calls the calculate_payroll method on each employee object
    """

    def calculate_payroll(self, employees: list):

        print('calculating payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'-Check Anount: {employee.calculate_payroll()}')
            print('\n')


# calculate_payroll methods called by PayrollSystem Class (employee.calculate_payroll)
class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hours_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate


class CommissionPolicy(SalaryPolicy):
    # init override
    def __init__(self, weekly_salary, commission):
        # get weekly_salary from SalaryPolicy
        super().__init__(weekly_salary)

        self.commission = commission

    def calculate_payroll(self):
        # execute calculate_payroll from parent
        fixed = super().calculate_payroll()
        return fixed + self.commission
