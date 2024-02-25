from datetime import datetime


class DataForTest:
    data_200 = {
        "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@yandex.ru',
        "password": "password",
        "name": "Username"
    }

    data_double = {
        "email": 'kov290583@yandex.ru',
        "password": "password",
        "name": "Username"
    }

    data_404 = {
        "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@yandex.ru',
        "password": "password",
        "name": ""
    }

    data_login_fail = {
        "login": "",
        "password": "1234"
    }

    data_user = {
        "email": "kov290583+23@yandex.ru",
        "password": "password",
        "name": "Stat"
    }

    updated_profile = {
        "email": "kov290583+23@yandex.ru",
        "password": "password",
        "name": "Oleg"
    }