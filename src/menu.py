
from os import system


def go_menu():
    action = '-1'

    while action != '0':

        print("""\
        1) Добавить запись
        2) Просмотр записей
        3) Поиск
        0) Выход
        """)

        action = input('Выберите действие.. ')

        if action == '1':
            pass
        elif action == '2':
            pass
        elif action == '3':
            pass
        elif action == '0':
            print('Выход')
        else:
            print('Неверный ввод. Повторите попытку')

        print()
