# https://www.hackerrank.com/challenges/the-minion-game

def main():
    s = input().strip()
    kevin = 0
    stuart = 0

    vowels = "AEIOU"
    slen = len(s)
    for i in range(slen):
        if vowels.find(s[i]) >= 0:
            kevin += (len(s) - i)
        else:
            stuart += (len(s) - i)

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")




if __name__ == '__main__':
    main()