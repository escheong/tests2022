# 2023년 까지만 출력

from pprint import pprint


def solution(month, date, weeks):
    date_by_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = date
    for i in range(month):
        total += date_by_month[i]

    day = total % 7 if total % 7 != 0 else 7   # 요일
    start_month = month if date - day >= 0 else month - 1
    if month == start_month:
        start_date = date - day + 1
    else:
        start_date = date_by_month[start_month] - (day - date) + 1

    answer = [[] for _ in range(weeks)]
    for i in range(weeks):
        if start_month > 12:
            break
        for j in range(7):
            if start_date <= date_by_month[start_month]:
                if i == 0 and j == 0:
                    answer[i].append(str(start_month) + "/" + str(start_date))
                else:
                    answer[i].append(str(start_date))

            else:
                start_month += 1
                start_date = 1
                if start_month > 12:
                    break
                answer[i].append(str(start_month) + "/" + str(start_date))

            start_date += 1

    return list(filter(None, answer))


pprint(solution(2, 14, 7))

# week     sun     mon     tue     wed     thur    fri     sat
#  1       '2/12   '13'    '14'    '15'    '16'    '17'    '18'
#  2       '19'    '20'    '21'    '22'    '23'    '24'    '25'
#  3       '26'    '27'    '28'    '3/1'   '2'     '3'     '4'
#  4       '5'     '6'     '7'     '8'     '9'     '10'    '11'
#  5       '12'    '13'    '14'    '15'    '16'    '17'    '18'
#  6       '19'    '20'    '21'    '22'    '23'    '24'    '25'
#  7       '26'    '27'    '28'    '29'    '30'    '31'    '4/1'
