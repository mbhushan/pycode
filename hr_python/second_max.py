# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
def main():
    n = int(input().strip())
    vals = set([int(x.strip()) for x in input().split(" ")])
    vals = list(vals)
    vals.sort(reverse=True)
    print(vals[1])

if __name__ == '__main__':
    main()