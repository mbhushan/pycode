"""
https://www.hackerrank.com/challenges/array-left-rotation

Input:
"5 2"
"1 2 3 4 5"

output:
3 4 5 1 2
"""
def main():
    (n, d) = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]

    arr = arr[d:] + arr[:d]
    print(' '.join(map(str, arr)))



if __name__ == '__main__':
    main()