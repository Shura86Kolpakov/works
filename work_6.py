# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие атрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Cars:
    def __init__(self, name, color, speed):
        self.speed = speed
        self.name = name
        self.color = color
        self._is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, _direction):
        self._direction = int(_direction)
        if self._direction > 0:
            print('Машина повернула направо')
        elif self._direction < 0:
            print('Машина повернула налево')
        else:
            print('Машина не поворачивает')


class TownCar(Cars):
    pass


class SportCar(Cars):
    pass


class WorkCar(Cars):
    pass


class PoliceCar(Cars):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self._is_police = True


car = PoliceCar('opel', 'white', 200)
car.go()
car.stop()
car.turn(-5)
print(car._is_police)

# Задача старая

# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import random


class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = random.randint(1, 10)
        self.armor = 0.7

    def _calculate_damage(self, who_attack, who_defend):
        self.who_attack = who_attack
        self.who_defend = who_defend
        return self.who_attack.damage // self.who_defend.armor

    def attack(self, who_attack, who_defend):
        self.who_attack = who_attack
        self.who_defend = who_defend
        self.damage = self._calculate_damage(who_attack, who_defend)
        who_defend.health -= self.damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack.name, who_defend.name, self.damage,
                                                                        who_defend.health))


class Player(Person):
    pass


class Enemy(Person):
    pass


player = Player(input('Введите имя: '))
enemy = Enemy(input('Введите имя: '))


def start_game():
    last_attacker = player
    while player.health > 0 and enemy.health > 0:
        if last_attacker == player:
            player.attack(player, enemy)
            last_attacker = enemy
        else:
            enemy.attack(enemy, player)
            last_attacker = player
    if player.health > 0:
        print(f'{player.name} победил!')
    else:
        print(f'{enemy.name} победил!')


start_game()

# player = {'name': input('Введите имя: '), 'health': 100, 'damage': 50}
# enemy = {'name': input('Введите имя: '), 'health': 100, 'damage': 50}
#
#
# def attack(who_attack, who_defend):
#     who_defend['health'] -= who_attack['damage']
#
#
# attack(player, enemy)
# print(enemy['health'], player['health'])
#
# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
#
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
#
#
# def generate_person_by_name(name, health=100, damage=50, armor=0.7):
#     return {'name': name, 'health': health, 'damage': damage, 'armor': armor}
#
#
# Описываем функцию для записи нашей структуры в файл.
# def write_person_to_file(person):
#     with open(person['name'], 'w', encoding='UTF-8') as f:
#         for key, value in person.items():
#             f.write('{} {}\n'.format(key, value))
#
#
# Описываем функцию для получения структуры из файла
# def get_person_by_filename(filename):
#     person = {}
#     with open(filename, encoding='UTF-8') as f:
#         for line in f:
#             key, value = line.split()
#             # Выполняем проверку на ключи, нам ведь нужны конкретные типы данных.
#             if key == 'armor':
#                 value = float(value)
#             elif key != 'name':
#                 value = int(value)
#             # Сохраняем значение по ключу.
#             person[key] = value

# return person


# Функция для подсчета урона
# def calculate_damage(damage, armor):
#     return damage // armor


# Функция атаки, принимает на вход 2 структуры
# def attack(who_attack, who_defend):
#     damage = calculate_damage(who_attack['damage'], who_defend['armor'])
#     who_defend['health'] -= damage
#     print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack['name'], who_defend['name'], damage,
#                                                                     who_defend['health']))


# Создаем наши структуры данных
# player = Player(input('Введите имя: '))
# enemy = Enemy(input('Введите имя: '))

# player = generate_person_by_name(player_name)
# enemy = generate_person_by_name(enemy_name)

# Записываем в файлы наши структуры
# write_person_to_file(player)
# write_person_to_file(enemy)


# Функция старта игры, никаких аргументов не принимает.
# def start_game():
# получаем наши структуры, через вышеописанную функцию
#     player = get_person_by_filename(player_name)
#     enemy = get_person_by_filename(enemy_name)

# Запоминаем кто последний атаковал
#     last_attacker = player
#     while player.health > 0 and enemy.health > 0:
#         if last_attacker == player:
#             player.attack(enemy, player)
#             last_attacker = enemy
#         else:
#             enemy.attack(player, enemy)
#             last_attacker = player
#
#     if player.health > 0:
#         print(f'{player.name} победил!')
#     else:
#         print(f'{enemy.name} победил!')


# start_game()
