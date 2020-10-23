# coding=utf-8
friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}

# допишите ваш код сюда
for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]

print('Лена живёт в городе ' + friends['Лена'])