# https://www.hackerrank.com/challenges/nested-list
def main():
    n = int(input().strip())
    # n = n * 2
    students = []
    marks_list = set()
    for i in range(0, n):
        name = input().strip()
        marks = float(input().strip())
        row = [name, marks]
        students.append(row)
        marks_list.add(marks)

    marks_list = list(marks_list)
    marks_list.sort()
    second_lowest = marks_list[1]
    result = set()
    for i in range(len(students)):
        if students[i][1] == second_lowest:
            result.add(students[i][0])
    # result.sort()
    result = sorted(result, key=lambda s: s.lower())
    # sorted(sorted(result), key=str.upper)
    for i in range(len(result)):
        print(result[i])


if __name__ == '__main__':
    main()