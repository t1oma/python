from klass import Persons
from random import choice

def ofor():
    print(f'Логин: {u.login}')
    print(f'Имя: {u.imya}')
    print(f'Фамилия: {u.falimia}')
    print(f'Посты: {u.posts}')

def select_user():
    # global u
    # u = choice(users)
    # while True:
    #     if u.login == current.login: # если выбрали сами себя
    #         u = choice(users)
    #     else:
    #         break
    global u
    while True:
        u = choice(users)
        if u.login == current.login: # если выбрали сами себя
            break


def session():
    select_user()
    while True:
        ofor()
        print('''[Возможные действия]: 
    - ПОДПИСКИ (посмотреть на кого подписан Ибрагим)
    - ПОДПИСЧИКИ (посмотреть кто подписан на Ибрагима)
    - ПОДПИСАТЬСЯ (стать подписчиком)
    - СЛЕДУЮЩИЙ аккаунт''')
        spros = input('> ').upper()
        if spros == "ВЫЙТИ":
            break
        elif spros == "СЛЕДУЮЩИЙ":
            select_user()
        elif spros == "ПОДПИСАТЬСЯ":
            current.podpiski += 1
            u.podpischiki += 1

a = Persons()
b = Persons("Чек")
c = Persons('степан', 'пропенко', 'yalox2323', 'jora1337')
users = [a, b, c]
print(ofor())
l = input('скажи логин: ')
p = input('скажи пароль: ')
for i in users:
    if i.log_in(l, p) == True:
        current = i
        session()
print(a.imya)

