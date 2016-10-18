# https://www.hackerrank.com/challenges/merge-the-tools

from collections import OrderedDict


def main():
    S = input().strip()
    step = int(input().strip())
    index = 0
    slen = len(S)
    vals = []
    while index <= slen:
        substr = S[index:index + step]
        key = "".join(OrderedDict.fromkeys(substr))
        vals.append(key)
        index = index + step
    for i in range(len(vals)):
        print(vals[i])


if __name__ == '__main__':
    main()