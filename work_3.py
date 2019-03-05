# easy1 функция возвращает строку
def data(x, y, z):
    print('{}, {} лет, проживает в городе {}'.format(x, y, z))


name = input('Введите Ваше имя:')
age = input('Укажите Ваш возраст:')
city = input('Введите Ваш город:')
data(name, age, city)

# easy2 функция принимает три числа возвращает большее
import random


def func_max(a, b, c):
    return max(a, b, c)


nums = []
for _ in range(3):
    nums.append(random.randint(-100, 100))
rezult = func_max(nums[0], nums[1], nums[2])
print('Были введены числа: {}; {}; {}.'.format(nums[0], nums[1], nums[2]))
print('Наибольшее:', rezult)


# easy3 ф-я приним. неск. строк, возвр. самую длинную
def func(*args):
    return max(*args, key=len)


a = input('Введите через пробел несколько строк: ')
c = func(a.split(' '))
print('Этa строка самая длинная -', c)


# normal
def accountant():
    lst = line.split('-')
    if int(lst[1]) < 500000:
        name = lst[0]
        salary = int(lst[1]) - int(lst[1]) * 0.13
        return f'{name.upper()} - {salary}\n'
    else:
        return ''


#
# names = ['Petr', 'Vadim', 'Oleg', 'Igor', 'Olga', 'Elena']
# salaries = [33343, 42781, 501355, 89670, 60543, 55489]
# salary_dict = dict(zip(names, salaries))

# file = open('salary.txt', 'w', encoding='utf-8')
# for key, value in salary_dict.items():
#     file.write(f'{key} - {value}\n')
# file.close()

with open('salary.txt', encoding='utf-8') as file:
    for line in file:
        new_line = accountant()
        print(new_line, end='')

# hard

# player = {'health': 100, 'armor': 1.2}
# enemy = {'health': 100, 'armor': 1.5}
# file = open('enemy.txt', 'w', encoding='utf-8')
# for key, value in enemy.items():
#     file.write(f'{key}:{value}\n')
# file.close()

player = {}
enemy = {}

with open('player.txt', encoding='utf-8') as file:
    for line in file:
        lst = line.split(':')
        player[str(lst[0])] = float(lst[1])
print('Player status', player)
with open('enemy.txt', encoding='utf-8') as file:
    for line in file:
        lst = line.split(':')
        enemy[str(lst[0])] = float(lst[1])
print('Enemy status', enemy)

import random


def attack(person):
    if person == player:
        punch = int(random.randint(0, 50) / enemy['armor'])
        damage = enemy['health'] - punch
        return damage
    else:
        punch = int(random.randint(0, 50) / player['armor'])
        damage = player['health'] - punch
        return damage


i = 1
while True:
    if i == 1:
        print('Атакует player')
        damage = attack(player)
        print('у enemy осталось:', damage, 'Health')
        if damage <= 0:
            enemy['health'] = damage
            print('Победил player')
            break
        else:
            enemy['health'] = damage
        i = 0
    else:
        print('Атакует enemy')
        damage = attack(enemy)
        print('у player осталось:', damage, 'Health')
        if damage <= 0:
            player['health'] = damage
            print('Победил enemy')
            break
        else:
            player['health'] = damage
        i = 1
print('Player status', player)
print('Enemy status', enemy)
