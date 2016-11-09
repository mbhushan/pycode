# https://www.hackerrank.com/challenges/compress-the-string


def main():
    s = input().strip()
    A = [int(x) for x in s]
    result = []
    last = A[0]
    alen = len(A)
    count = 0
    for i in range(1, alen):
        if A[i] == last:
            count += 1
        else:
            result.append((count+1, last))
            last = A[i]
            count = 0

    if count != 0:
        result.append((count+1, last))

    for t in result:
        print(t, end=" ")


if __name__ == '__main__':
    main()