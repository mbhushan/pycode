# https://www.hackerrank.com/challenges/python-mutations
s = input().strip()
args = [x for x in input().split(" ")]
index = int(args[0].strip())
value = args[1].strip()
L = list(s)
L[index] = value
print("".join(L))