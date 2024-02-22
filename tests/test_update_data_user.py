import allure
import json
import requests
from data_test.constants import Constants

headers = {"Content-Type": "application/json"}


data = {
    "email": "kov290583+23@yandex.ru",
    "password": "password",
    "name": "User"
}

updated_profile = {
            "email": 'kov290583+23@yandex.ru',
            "password": "password",
            "name": "Oleg"
        }


@allure.epic("Обновление данных юзера")
@allure.feature("Обновляем имя пользователя")
class TestUpdateDataUser:
    @allure.step("Получаем авторизационный токен и записываем его в переменную")
    def get_token(self):
        token = requests.post(Constants.URL + Constants.END_POINT_LOGIN_USER, headers=headers,
                              data=json.dumps(data))
        new_token = token.json()['accessToken']
        return new_token

    @allure.story("PATCH запрос на обновление данных юзера")
    @allure.title('Проверка авторизации в системе с валидными и невалидными данными')
    @allure.description("В этом тесте м ыотправляем обновление данных юзера. Меняем имя.")
    @allure.tag("NewAPI", "Essentials", "UpdateCourier")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://stellarburgers.nomoreparties.site", name="Website")
    @allure.issue("UpdateUser-05")
    @allure.testcase("TMS-05")
    @allure.step("Отправка PATCH запроса - с измененными данными")
    def test_updated_profile(self):
        new_token = self.get_token()
        response = requests.patch(Constants.URL + Constants.END_POINT_UPDATE_USER,
                                  headers={'Authorization': new_token}, data=updated_profile)

        assert response.status_code == 200
        assert response.json()['user']['name'] == 'Oleg'
