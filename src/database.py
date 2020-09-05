from re import IGNORECASE
from datetime import datetime
from tinydb import TinyDB, Query


PATH_TO_DB = 'resources/db.json'


def interactive_put():

    name = input("Введите название предмета.. ")
    desc = input("Введите описание (опционально).. ")
    if desc == '':
        desc = 'Пропущено'
    locate = input("Введите местоположение.. ")
    date = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    put(name, desc, date, locate)


# insert item into database
def put(name, desc, date, locate):
    with TinyDB(PATH_TO_DB) as db:
        db.insert({'name': name, 'desc': desc, 'date': date, 'locate': locate})


def get_all():
    print()
    with TinyDB(PATH_TO_DB) as db:
        data = db.all()
    for i in data:
        print('Имя: ', i.get('name'), sep='')
        print('Описание: ', i.get('desc'), sep='')
        print('Местоположение: ', i.get('locate'), sep='')
        print('Дата обновления: ', i.get('date'), sep='')
        print()


# search by name
def interactive_search():
    name = input('Введите название предмета.. ')
    search(name)


def search(name):

    with TinyDB(PATH_TO_DB) as db:
        result = db.search(Query().name.matches(name, flags=IGNORECASE))

    for i in result:
        print()
        print('Имя: ', i.get('name'), sep='')
        print('Описание: ', i.get('desc'), sep='')
        print('Местоположение: ', i.get('locate'), sep='')
        print('Дата обновления: ', i.get('date'), sep='')
