# https://www.hackerrank.com/challenges/capitalize
s = input().strip().split(" ")

words = []
for i in range(len(s)):
    words.append(s[i].capitalize())

print(" ".join(words))