# https://www.hackerrank.com/challenges/write-a-function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False

    # Write your logic here

    return leap