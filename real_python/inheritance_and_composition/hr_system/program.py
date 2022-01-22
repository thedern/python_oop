# entry point into our hr application

import employees
import hr
import productivity


# run payroll


def payroll():
    """
    run payroll by creating instances of employees and running their pay
    :return:
    :rtype:
    """

    manager = employees.Manager(1, 'John Smith', 1500)
    secretary = employees.Secretary(2, 'Jane Doe', 1200)
    sales_person = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
    factory_worker = employees.FactoryWorker(4, 'Peter Pan', 40, 15)
    temporary_secretary = employees.TemporarySecretary(5, 'Mary Poppins', 40, 10)

    workers = [manager, secretary, sales_person, factory_worker, temporary_secretary]

    # create instance of payroll system
    payroll_system = hr.PayrollSystem()
    # calculate_payroll runs the pay calculation for each employee object.
    payroll_system.calculate_payroll(workers)

    # create instance of productivity system
    productivity_system = productivity.ProductivitySystem()
    # call track method of productivity system object and pass in 40 hours
    productivity_system.track(workers, 40)


if __name__ == "__main__":
    # if file is run directly its name is '__main__', else imported, its name os <filename>
    print(f'file name is {__name__}\n')
    payroll()
