# https://www.hackerrank.com/challenges/py-set-difference-operation
def main():
    n = int(input())
    E = set(int(x) for x in input().split(" "))
    m = int(input())
    F = set(int(x) for x in input().split(" "))
    ans = E - F
    print(len(ans))


if __name__ == '__main__':
    main()