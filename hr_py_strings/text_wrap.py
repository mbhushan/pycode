# https://www.hackerrank.com/challenges/text-wrap
import textwrap

S = input().strip()
width = int(input().strip())
print(textwrap.fill(S,width))