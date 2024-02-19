from datetime import datetime


class DataForTest:
    data_200 = {
        "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@yandex.ru',
        "password": "password",
        "name": "Username"
    }

    data_403 = {
        "email": 'kov290583@yandex.ru',
        "password": "password",
        "name": "Username"
    }

    data_404 = {
        "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@yandex.ru',
        "password": "password",
        "name": ""
    }