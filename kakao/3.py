import itertools
from itertools import product


def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)

    sets = [10, 20, 30, 40]
    tmp = itertools.product(sets, repeat=m)

    # 유저별 구매액 계산
    def calc_total(perc, now):
        total = 0
        for i in range(m):
            if now <= perc[i]:
                total += (100-perc[i])/100*emoticons[i]
        return total

    answer = []
    for perc in tmp:
        plus = 0
        sales = 0

        for i in range(n):
            total = calc_total(perc, users[i][0])
            if users[i][1] <= total:
                plus += 1
            else:
                sales += total

        answer.append([plus, int(sales)])

    answer.sort()

    return answer[-1]


print(solution(
    [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
