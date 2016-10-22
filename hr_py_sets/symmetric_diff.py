# https://www.hackerrank.com/challenges/symmetric-difference
def main():
    n = input().split(" ")
    A = [int(x) for x in input().split(" ")]
    m = input().split(" ")
    B = [int(y) for y in input().split(" ")]
    aset = set(A)
    bset = set(B)
    result_set = aset ^ bset
    result_set = list(result_set)
    result_set.sort()
    for x in result_set:
        print(x)


if __name__ == '__main__':
    main()