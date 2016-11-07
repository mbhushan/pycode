#https://www.hackerrank.com/challenges/itertools-product

from itertools import product

def main():
    A = [int(x) for x in input().strip().split(" ")]
    B = [int(x) for x in input().strip().split(" ")]
    ans = list(product(A, B))
    for x in ans:
        print(x, end=" ")


if __name__ == '__main__':
    main()