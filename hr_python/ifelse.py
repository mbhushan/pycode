#!/bin/python3

import sys

"""
https://www.hackerrank.com/challenges/py-if-else
"""


def main():
    N = int(input().strip())
    if N % 2 == 1:
        print("Weird")
    elif (N >= 2 and N <= 5) or (N > 20):
        print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    main()
