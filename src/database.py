from re import IGNORECASE
from datetime import datetime
from tinydb import TinyDB, Query


PATH_TO_ITEMS_DB = 'resources/objects_db.json'
PATH_TO_USERS_DB = 'resources/users_db.json'


def get_length(path):
    with TinyDB(path) as item_db:
        return len(item_db)


def interactive_put_item():

    name = input("Введите название предмета.. ")
    desc = input("Введите описание (опционально).. ")
    remark = input("Введите примечание (опционально).. ")
    if desc == '':
        desc = 'Пропущено'
    locate = input("Введите местоположение.. ")
    date = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    put_item(name, desc, remark, date, locate)


# insert item into database
def put_item(name, desc, remark, date, locate):
    with TinyDB(PATH_TO_ITEMS_DB) as item_db:
        item_db.insert({'id': get_length(PATH_TO_ITEMS_DB), 'name': name, 'desc': desc, 'remark': remark,
                        'date': date, 'location': locate, 'who_uses': 'None'})


def interactive_put_user():
    username = input('Введите имя нового пользователя.. ')
    put_user(username)


def put_user(username):
    with TinyDB(PATH_TO_USERS_DB) as users_db:
        users_db.insert({'id': get_length(PATH_TO_ITEMS_DB), 'name': username})


def get_all():
    print()

    with TinyDB(PATH_TO_USERS_DB) as users_db:
        data = users_db.all()
    print('Список зарегистрированных пользователей:')
    if not data:
        print('Никого нету')

    else:
        for i in data:
            print(i.get('name'))
    print()

    with TinyDB(PATH_TO_ITEMS_DB) as item_db:
        data = item_db.all()

    print('Список предметов:')
    if not data:
        print('Ничего нету')
    else:
        for i in data:
            beauty_record_output(i)


# search by name
def interactive_search():
    name = input('Введите название предмета.. ')
    search(name)


def search(name):
    with TinyDB(PATH_TO_ITEMS_DB) as items_db:
        result = items_db.search(Query().name.matches(name, flags=IGNORECASE))

    for i in result:
        beauty_record_output(i)


def beauty_record_output(record_dict):
    if not record_dict:
        print('Ничего нету')
        return

    print()
    print('Имя: ', record_dict.get('name'), sep='')
    if record_dict.get('desc') != '':
        print('Описание: ', record_dict.get('desc'), sep='')
    if record_dict.get('remark') != '':
        print('Примечание: ', record_dict.get('remark'), sep='')
    print('Местоположение: ', record_dict.get('location'), sep='')
    print('Дата регистрации: ', record_dict.get('date'), sep='')
    if record_dict.get('who_uses') == 'None':
        print('В данный никем не импользуется')
    else:
        with TinyDB(PATH_TO_USERS_DB) as users_db:
            username = users_db.search(Query().id == int((record_dict.get('who_uses')))).get('name')
        print('Предмет используется пользователем "' + username + '"')
    print()
