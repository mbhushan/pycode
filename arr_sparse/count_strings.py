
def main():
    n = int(input())
    buff = []
    for i in range(n):
        buff.append(input())

    q = int(input())
    result = []
    for i in range(q):
        key = input()
        freq = buff.count(key)
        result.append(freq)
        print(freq)


if __name__ == '__main__':
    main()