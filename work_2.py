# print('hello')

# Нумерованный писок фруктов
#fruits = ['яблоко', 'банан', 'киви', 'арбуз']
#i = 0
#for fruit in fruits:
#    i += 1
#    print('{}. ''{}'.format(i, fruit))

# удаление элементов одного списка из другого
#products = ['яблоко', 'банан', 'киви', 'арбуз', 'молоко', 'хлеб', 'сыр']
#fruits = ['яблоко', 'банан', 'киви', 'арбуз', 'апельсин']

# создание нового списка
numbers = [1, 3, 4, 56, 78, 45, 345, 12, 0]
new_numbers = []

for _ in numbers:
    if _ % 2 == 0:
        new_numbers.append(_ / 4)
    else:
        new_numbers.append(_ * 2)

print(new_numbers)
