# https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations

def main():
    a, b = input().strip().split(" ")
    b = int(b)
    a = sorted(a)
    ans = list(permutations(a, b))
    for x in ans:
        print(''.join(x))




if __name__ == '__main__':
    main()