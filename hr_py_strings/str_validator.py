# https://www.hackerrank.com/challenges/string-validators

def main():
    S = input()
    ans = [False] * 5
    for i in range(len(S)):
        x = S[i]
        if x.isalnum():
            ans[0] = True
        if x.isalpha():
            ans[1] = True
        if x.isdigit():
            ans[2] = True
        if x.islower():
            ans[3] = True
        if x.isupper():
            ans[4] = True
    # print(ans)
    for i in range(len(ans)):
        print(ans[i])


if __name__ == '__main__':
    main()