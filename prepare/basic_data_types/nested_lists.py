#!/usr/bin/env python3

def second_lowest_grade(grades_list:list) -> float:
    if len(grades_list) == 0:
        raise ValueError
    elif len(grades_list) <= 1:
        return grades_list[0][1]
    score_list = [x[1] for x in grades_list]
    min_value = min(score_list)
    score_list = sorted(score_list)
    for value in score_list:
        if value > min_value:
            return value
    return min_value


if __name__ == '__main__':
    grades_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades_list.append([name, score])
    slg = second_lowest_grade(grades_list)
    students_list = []
    for item in grades_list:
        if item[1] == slg:
            students_list.append(item[0])
    students_list = sorted(students_list)
    for name in students_list:
        print(name)
