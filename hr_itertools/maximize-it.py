# https://www.hackerrank.com/challenges/maximize-it



def main():
    (K, M) = (int(x) for x in input().strip().split(" "))
    X = 0
    for i in range(K):
        n = max([int(x) for x in input().strip().split(" ")])
        X += ((n*n) % 1000)
    print (X)





if __name__ == '__main__':
    main()