# coding=utf-8
def calc_stat(listened):  # от англ. calculate statistics, посчитать статистику
    result = 0
    for item in listened:
        result = result + item
    return f'Вы прослушали {len(listened)} песен, общей продолжительностью {result // 60} минут и {result % 60} секунд.'


print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))
