# https://www.hackerrank.com/challenges/py-set-discard-remove-pop
def main():
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    for i in range(m):
        args = input().strip().split(" ")
        if args[0] == "pop" and len(s) > 0:
            s.pop()
        elif args[0] == "remove" and int(args[1]) in s:
            s.remove(int(args[1]))
        elif args[0] == "discard":
            s.discard(int(args[1]))
    print(sum(s))



if __name__ == '__main__':
    main()