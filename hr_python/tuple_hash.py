# https://www.hackerrank.com/challenges/python-tuples
def main():
    n = int(input().strip())
    args = tuple([int(x) for x in input().split(" ")])
    print(hash(args))

if __name__ == '__main__':
    main()