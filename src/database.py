
from datetime import datetime


data = list()


def interactive_put():
    name = input("Введите название предмета.. ")
    desc = input("Введите описание (опционально).. ")
    if desc == '':
        desc = 'Пропущено'
    locate = input("Введите местоположение.. ")
    date = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    put(name, desc, date, locate)


def put(name, desc, date, locate):
    data.append({'name': name, 'desc': desc, 'date': date, 'locate': locate})


def get_all():
    print()
    for i in data:
        print('Имя: ', i.get('name'), sep='')
        print('Описание: ', i.get('desc'), sep='')
        print('Местоположение: ', i.get('locate'), sep='')
        print('Дата обновления: ', i.get('date'), sep='')
        print()
