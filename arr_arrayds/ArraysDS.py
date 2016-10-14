#import sys

from ArraysOp import ArraysOp


def main():
    """Given an array, , of  integers, print each element in reverse order
    as a single line of space-separated integers."""
    (n, arr) = readInput()
    obj = ArraysOp(n, arr)
    arr = obj.reverseArr()
    print(' '.join(map(str, arr)))



def readInput():
    n = int(input())
    arr = [int(i) for i in input().split()]
    #print(n)
    #print(arr)
    return (n, arr)



if __name__ == '__main__':
    main()