
import src.database as db


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
        print()

        if action == '1':
            db.interactive_put()
        elif action == '2':
            db.get_all()
        elif action == '3':
            pass
        elif action == '0':
            print('Выход')
        else:
            print('Неверный ввод. Повторите попытку')
        print()
