# coding=utf-8
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif 6 <= current_hour <= 11:
        print('Доброе утро!')
    elif 12 <= current_hour <= 17:
        print('Добрый день!')
    elif 18 <= current_hour <= 22:
        print('Добрый вечер!')


say_hello(4)
say_hello(10)
