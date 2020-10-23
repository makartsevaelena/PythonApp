# coding=utf-8
def print_shopping_list(pizza, salad):
    products = set(pizza.keys()).union(set(salad.keys()))
    shopping_list = {}
    for item in products:
        massa = 0
        if item in pizza.keys():
            massa = massa + pizza[item]
        if item in salad.keys():
            massa = massa + salad[item]
            shopping_list[item] = massa
        else:
            shopping_list[item] = massa
    for product, massa in shopping_list.items():
        text = product + ': ' + str(massa) + '\n'
        print(text)

pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)
