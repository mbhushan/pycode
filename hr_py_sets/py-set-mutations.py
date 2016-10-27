import  copy

# https://www.hackerrank.com/challenges/py-set-mutations

def main():
    size = int(input().strip())
    fset = set([int(x) for x in input().strip().split(" ")])
    n = int(input())
    for i in range(n):
        L = [str(x) for x in input().strip().split(" ")]
        second_set = set([int(x) for x in input().strip().split(" ")])
        if L[0] == "intersection_update":
            fset.intersection_update(second_set)
        if L[0] == "update":
            fset.update(second_set)
        if L[0] == "symmetric_difference_update":
            fset.symmetric_difference_update(second_set)
        if L[0] == "difference_update":
            fset.difference_update(second_set)

    print(sum(fset))
        # first_set = fset.copy()

if __name__ == '__main__':
    main()