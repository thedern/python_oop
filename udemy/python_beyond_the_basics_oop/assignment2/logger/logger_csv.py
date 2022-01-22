# from udemy.python_beyond_the_basics_oop.assignments.assignment2.helper_classes.util_classes import Logfile, Delimfile

from assignment2 import util_classes


def test():
    log = util_classes.Logfile('log.txt')
    c = util_classes.Delimfile('text.csv', ',')

    log.write('this is another log message')
    log.write('this is yet another log message')

    c.write(['a', 'b', 'c', 'd'])
    c.write(['1', '2', '3', '4'])

