# https://www.hackerrank.com/challenges/itertools-combinations

from itertools import combinations

def main():
    a, b = input().strip().split(" ")
    b = int(b)
    a = sorted(a)
    for i in range(b):
        ans = list(combinations(a, i+1))
        for x in ans:
            print(''.join(x))




if __name__ == '__main__':
    main()