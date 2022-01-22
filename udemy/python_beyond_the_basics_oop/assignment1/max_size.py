
class MaxSize(object):

    def __init__(self, max_len):
        self.ls1 = []
        self.max_len = max_len

    def push(self, val):
        if len(self.ls1) < self.max_len:
            self.ls1.append(val)

    def get_list(self):
        return self.ls1
