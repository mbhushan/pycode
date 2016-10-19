# https://www.hackerrank.com/challenges/finding-the-percentage
def main():
    n = int(input().strip())
    score = dict()
    for i in range(n):
        vals = [x.strip() for x in input().split(" ")]
        key = vals[0]
        marks = float(0)
        for j in range(1, len(vals)):
            marks += float(vals[j])
        marks = marks / (len(vals) - 1)
        value = round(marks, 2)
        score[key] = value
    q = input().strip()
    print("%.2f" % score[q])


if __name__ == '__main__':
    main()