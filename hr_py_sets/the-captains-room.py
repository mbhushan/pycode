# https://www.hackerrank.com/challenges/py-the-captains-room

def main():
    K = int(input().strip())
    stream = [int(x) for x in input().split(" ")]
    map = {}
    for x in stream:
        count = 0
        if x in map:
            count = map.get(x)
        map[x] = count + 1

    for key in map:
        if map[key] == 1:
            print(key)



if __name__ == '__main__':
    main()