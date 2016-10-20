# https://www.hackerrank.com/challenges/py-introduction-to-sets
def main():
    numplants = int(input().strip())
    heights = [int(x) for x in input().split(" ")]
    plants = set(heights)
    total_sum = sum(plants)
    avg = total_sum / len(plants)
    print(avg)


if __name__ == '__main__':
    main()