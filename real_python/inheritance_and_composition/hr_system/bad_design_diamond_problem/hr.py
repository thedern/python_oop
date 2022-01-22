
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


print(f'file name is: {__name__}')
