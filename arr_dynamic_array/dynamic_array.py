"""
https://www.hackerrank.com/challenges/dynamic-array
Input:
"2 5"
"1 0 5"
"1 1 7"
"1 0 3"
"2 1 0"
"2 1 1"

Output:
7
3
"""

class DynamicArray(object):

    def __init__(self, n):
        self.arr = [[] for i in range(n)]
        self.last_ans = 0

    def setval(self, index, value):
        self.arr[index] = value

    def get_lastans(self):
        return self.last_ans

    def set_lastans(self, value):
        self.last_ans = value

    def append_seq(self, seq, y):
        self.arr[seq].append(y)

    def get_arrval(self, seq, y):
        size = len(self.arr[seq])
        return self.arr[seq][y % size]


def main():
    (n, q) = [int(i) for i in input().split()]
    obj = DynamicArray(n)
    for arr_i in range(q):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        # print(arr_t)
        x = arr_t[1]
        y = arr_t[2]
        #print("x: ", x , " y: ", y)
        last_ans = obj.get_lastans()
        #print("last ans: ", last_ans)
        seq = x ^ int(last_ans)
        seq = seq % n

        if arr_t[0] == 1:
            obj.append_seq(seq, y)
        if arr_t[0] == 2:
            val = obj.get_arrval(seq, y)
            obj.set_lastans(val)
            print(val)





if __name__ == '__main__':
    main()