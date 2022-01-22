

class ProductivitySystem:
    """
    productivitySystem's track method calls the 'work' method on each employee roll object
    """
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('\n')
