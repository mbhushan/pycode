def find_count(S, P):
    flag = True
    index = 0
    count = 0
    while flag:
        index = S.find(P, index)
        if index == -1:
            flag = False
        else:
            count = count + 1
        index = index + 1

    return count

def main():
    s = input().strip()
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    slen = len(s)
    for i in range(slen):
        if vowels.find(s[i]) >= 0:
            L = 1
            while L <= len(s[i:]):
                kevin = kevin + find_count(s[i:], s[i:i+L])
                L = L + 1
        else:
            L = 1
            while L <= len(s[i:]):
                stuart = stuart + find_count(s[i:], s[i:i+L])
                L = L + 1
    print("kevin: ", kevin)
    print("stuart: ", stuart)




if __name__ == '__main__':
    main()