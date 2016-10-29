# https://www.hackerrank.com/challenges/py-check-subset

def main():
    n = int(input())
    for i in range(n):  # More than 4 lines will result in 0 score. Blank lines won't be counted.
        a = int(input())
        A = set(input().split())
        b = int(input())
        B = set(input().split())
        ans = True
        for x in A:
            if x not in B:
                ans = False
        print(ans)

if __name__ == '__main__':
    main()