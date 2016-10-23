# https://www.hackerrank.com/challenges/python-lists

def main():
    n = int(input().strip())
    A = []
    for i in range(n):
        cmd = [x for x in input().split(" ")]
        if cmd[0] == "insert":
            index = int(cmd[1])
            value = int(cmd[2])
            A.insert(index, value)
        elif cmd[0] == "append":
            value = int(cmd[1])
            A.append(value)
        elif cmd[0] == "remove":
            value = int(cmd[1])
            A.remove(value)
        elif cmd[0] == "sort":
            A.sort()
        elif cmd[0] == "pop":
            A.pop()
        elif cmd[0] == "reverse":
            A.reverse()
        elif cmd[0] == "print":
            print(A)


if __name__ == '__main__':
    main()

