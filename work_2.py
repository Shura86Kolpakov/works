﻿# print('hello')

# Нумерованный писок фруктов
#fruits = ['яблоко', 'банан', 'киви', 'арбуз']
#i = 0
#for fruit in fruits:
#    i += 1
#    print('{}. ''{}'.format(i, fruit))

# удаление элементов одного списка из другого
# products = ['яблоко', 'банан', 'киви', 'арбуз', 'молоко', 'хлеб', 'сыр']
# fruits = ['яблоко', 'банан', 'киви', 'арбуз', 'апельсин']
# products_1 = ['яблоко', 'банан', 'киви', 'арбуз', 'молоко', 'хлеб', 'сыр']
#
# for i in products_1:
#     for j in fruits:
#         if i == j:
#             products.remove(i)
# print(products)

# создание нового списка
# numbers = [1, 3, 4, 56, 78, 45, 345, 12, 0]
# new_numbers = []
#
# for _ in numbers:
#     if _ % 2 == 0:
#         new_numbers.append(_ / 4)
#     else:
#         new_numbers.append(_ * 2)
#
# print(new_numbers)

# расчет координаты y
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# y = -12 * x + 11111140.2121
# print(y)

# Создание списка по результатам извлечения корней
# numbers = [1, 3, 4, 56, -78, 45, 441, 12, 0]
# new_numbers = []
# for i in numbers:
#     if i < 0:
#         continue
#     else:
#         n = i ** 0.5
#         if float.is_integer(n):
#             new_numbers.append(round(n))
# print(new_numbers)



# Задача №2 перевод даты
# a = input('введите дату(дд.мм.гггг): ')
# year = a[6:]
# month = a[3:5]
# day = a[:2]
# days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
#         '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
#         '11': 'одинадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
#         '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
#         '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
#         '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое',
#         '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
#         '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
# months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
#         '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
#         '11': 'ноября'}
# for key, value in days.items():
#     if key == day:
#         dd = value
# for key, value in months.items():
#     if key == month:
#         mm = value
# print('{} {} {} года'.format(dd, mm, year))



#Задача №3 самозаполняющийся список

# import random
#
# n = int(input('Введите число элементов списка: '))
#
# lst = []
# for i in range(1, n + 1):
#     lst.append(random.randint(-100, 100))
#
# print(lst)


# Задача №4 Преобразование списка
# а) новый список не содержит дублей
# lst = [1, 2, 4, 5, 6, 2, 5, 2]
# a = set(lst)
# lst2 = list(a)
# print(lst2)


# б) новый список не содержит повторяющихся элементов
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst_1 = []
tup_lst = tuple(lst)
for i in tup_lst:
        for j in tup_lst[i:]:
            if i == j:
                lst_1.append(i)
                break
set_lst_1 = set(lst_1)
set_lst = set(lst)
set_lst_2 = set_lst - set_lst_1
lst_2 = list(set_lst_2)
print("lst_2 =", lst_2)