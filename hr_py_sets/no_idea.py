# https://www.hackerrank.com/challenges/no-idea

def main():
    (n, m) = (int(x) for x in input().split(" "))
    stream = [int(x) for x in input().split(" ")]
    A = set(int(x) for x in input().split(" "))
    B = set(int(x) for x in input().split(" "))
    happiness = 0
    # A = set(A)
    # B = set(B)
    for x in stream:
        if x in A:
            happiness += 1
        if x in B:
            happiness -= 1
    print(happiness)



if __name__ == '__main__':
    main()