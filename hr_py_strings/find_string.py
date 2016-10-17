# https://www.hackerrank.com/challenges/find-a-string
def main():
    S = input().strip()
    P = input().strip()
    index = 0
    count = 0
    flag = True
    while flag:
        index = S.find(P, index)
        if index == -1:
            flag = False
        else:
            count = count + 1
        index = index + 1

    print(count)


if __name__ == '__main__':
    main()