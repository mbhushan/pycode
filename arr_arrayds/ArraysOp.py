
class ArraysOp(object):

    def __init__(self, len, arr):
        self.len = len
        self.arr = arr

    def reverseArr(self):
        self.arr = self.arr[::-1]
        return self.arr