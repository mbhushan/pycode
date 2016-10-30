# https://www.hackerrank.com/challenges/py-check-strict-superset

def main():
    A = set([int(x) for x in input().strip().split(" ")])
    n = int(input().strip())
    ans = True
    for i in range(n):
        B = A.copy()
        C = set([int(x) for x in input().strip().split(" ")])
        if B.issuperset(C):
            B.difference_update(C)
            if len(B) < 1:
                ans = False
                break
        else:
            ans = False
            break
    if ans:
        print("True")
    else:
        print("False")



if __name__ == '__main__':
    main()