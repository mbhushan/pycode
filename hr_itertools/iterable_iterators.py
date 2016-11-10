# https://www.hackerrank.com/challenges/iterables-and-iterators

from itertools import combinations

def main():
    N = int(input().strip())
    A = [x for x in input().strip().split(" ")]
    K = int(input().strip())
    #A = ''.join(A)
    r = list(combinations(A, K))
    x = 'a'

    alen = len(r)
    print (r)
    total = sum([1 for i in r if x in i])

    ans = (total * 1.0) / alen
    print(ans)



if __name__ == '__main__':
    main()