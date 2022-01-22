import abc
from abc import ABC
from datetime import datetime


class FileWriter(object):
    """
    parent abstract class not meant to be instantiated but used but other classes
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write_file(self):
        return

    def __init__(self, filename):
        # takes a filename upon initialization
        self.filename = filename

    # write file to disk
    def write_line(self, text):
        with open(self.filename, 'a') as fh:
            fh.write(text + '\n')


# child
class Logfile(FileWriter, ABC):
    # gets init from parent which contains filename

    # instance method that calls parent's write_line after formatting date
    # instance takes a string argument and writes it to the file
    def write(self, this_line):
        # get current datetime
        dt = datetime.now()
        date_str = dt.strftime('%y-%m-%d %H:%M')
        # write_line from parent, opens file, writes text
        self.write_line(f'{date_str} {this_line}')


# child
class Delimfile(FileWriter, ABC):
    # takes filename and delimiter as args
    def __init__(self, filename, delim):
        # gets the filename from the parent
        super(Delimfile, self).__init__(filename)
        self.delim = delim

    # instance method takes list as arg and writes list using parent write_line method
    def write(self, this_list):
        line = self.delim.join(this_list)
        # gets write_line from parent
        self.write_line(line)
