# easy_1
import random

lst_1 = [random.randint(-10, 10) for i in range(10)]
lst_2 = [i**2 for i in lst_1]
print(lst_1)
print(lst_2)

# easy_2
fruits_1 = ['apple', 'orange', 'peach', 'mango']
fruits_2 = ['lemon', 'peach', 'banana', 'apple']
fruits_3 = [fruit for fruit in fruits_1 if fruit in fruits_2]
print(fruits_3)


# easy_3
import random

lst_1 = [random.randint(-10, 10) for i in range(10)]
lst_2 = [i for i in lst_1 if i % 3 == 0 and i % 4 != 0 and i > 0]
print(lst_1)
print(lst_2)

# normal_1
import re
pattern = '[А-ЯA-Z]'
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
name = (name.title() if re.match(pattern, name) is None else name)
surname = (surname.title() if re.match(pattern, name) is None else surname)
pattern = '[a-z_0-9]+@[a-z]+\.(com|org|ru)'

while True:
    email = input('Введите email: ')
    pattern = '[a-z_0-9]+@[a-z]+\.(com|org|ru)'
    if re.match(pattern, email) is None:
        print('Неправильный email')
    else:
        break
print(f'{name} {surname} {email}')

# normal_2
import re
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный -
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела -
А нынче.... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern = '[\.]{2,}'
if (re.search(pattern, some_str)) is None:
    print('многоточия нет')
else:
    print('многоточие есть')
