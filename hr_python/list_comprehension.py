# https://www.hackerrank.com/challenges/list-comprehensions

def main():
    x = int(input().strip())
    y = int(input().strip())
    z = int(input().strip())
    n = int(input().strip())
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(ans)


if __name__ == '__main__':
    main()