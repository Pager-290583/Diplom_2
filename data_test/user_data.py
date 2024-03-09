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
        "password": ""
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

    data_ingridient = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    data_not_ingridient = {
        "ingredients": []
    }

    data_bad_ingridient = {
        "ingredients": ["61c0c5a71d1f82001bdaaa61", "61c0c5a71d1f82001bdaaa61"]
    }