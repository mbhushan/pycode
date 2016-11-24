from collections import Counter


def main():
    mylist = input().strip().split(",")
    print(mylist)
    print(Counter(mylist))


if __name__ == '__main__':
    main()


