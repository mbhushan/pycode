import numpy as np
import sys

"""
Given a 6x6 2D Array A, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

"1 1 1 0 0 0"
"0 1 0 0 0 0"
"1 1 1 0 0 0"
"0 0 2 4 4 0"
"0 0 0 2 0 0"
"0 0 1 2 4 0"
output: 19
"1 1 1 0 0 0"
"0 1 0 0 0 0"
"1 1 1 0 0 0"
"0 9 2 -4 -4 0"
"0 0 0 -2 0 0"
"0 0 -1 -2 -4 0"
output: 13

"0 -4 -6 0 -7 -6"
"-1 -2 -6 -8 -3 -1"
"-8 -4 -2 -8 -8 -6"
"-3 -1 -2 -5 -7 -4"
"-3 -5 -3 -6 -6 -6"
"-3 -6 0 -8 -6 -7"
"""

class HourGlass(object):

    def __init__(self, matrix):
        self.matrix = matrix


    def max_sum(self):
        row = len(self.matrix)
        col = len(self.matrix[0])
        #print("row: " , row , " col" , col)
        count = -sys.maxsize
        for i in range(row - 2):
            for j in range(col - 2):
                s = 0
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        s = s + self.matrix[x][y]
                s = s - (self.matrix[i+1][j] + self.matrix[i+1][j+2])
                count = max(count, s)
        return count



    def count_hour_glass(self):
        if self.matrix is None:
            return 0

        row = len(self.matrix)
        col = len(self.matrix[0])

        if (row < 3 or col < 3):
            return 0;

        count = -sys.maxsize
        m = np.array(self.matrix)
        (a, b) = m.shape

        for i in range(a - 2):
            for j in range(b - 2):
                d = m[i:i + 3, j:j + 3]
                s = sum(sum(d))
                s = s - (d[1][0] + d[1][2])
                count = max(count, s)

        return count


def main():
    arr = []
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
    glass = HourGlass(arr)
    print(arr)
    print(glass.count_hour_glass())
    print(glass.max_sum())


if __name__ == '__main__':
    main()
