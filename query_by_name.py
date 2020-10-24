# coding=utf-8
def check_query(query):
    # напишите код тела функции
    query_list = query.split(', ')
    if query_list[0] == 'Анфиса':
        text = 'запрос к Анфисе'
    else:
        text = 'запрос к кому-то ещё'
    return text


# дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '-', result)
