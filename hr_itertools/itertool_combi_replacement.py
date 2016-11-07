# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement


def main():
    a, b = input().strip().split(" ")
    b = int(b)
    a = sorted(a)
    ans = list(combinations_with_replacement(a, b))
    for x in ans:
        print(''.join(x))

if __name__ == '__main__':
    main()