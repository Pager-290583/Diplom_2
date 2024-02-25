import allure
import pytest
import json
import requests
from data_test.constants import Constants
from data_test.user_data import DataForTest


@allure.epic("Обновление данных юзера")
@allure.feature("Обновляем имя пользователя")
class TestUpdateDataUser:
    @allure.step("Получаем авторизационный токен и записываем его в переменную")
    def get_token(self):
        token = requests.post(Constants.URL + Constants.END_POINT_LOGIN_USER, headers=Constants.headers,
                              data=json.dumps(DataForTest.data_user))
        new_token = token.json()['accessToken']
        return new_token

    @allure.story("PATCH запрос на обновление данных юзера с авторизацией")
    @allure.title('Проверка авторизации в системе с валидными и невалидными данными')
    @allure.description("В этом тесте мы отправляем обновление данных юзера. Меняем имя.")
    @allure.tag("NewAPI", "Essentials", "UpdateUser")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://stellarburgers.nomoreparties.site", name="Website")
    @allure.issue("UpdateUser-05")
    @allure.testcase("TMS-05")
    @allure.step("Получаем токен и отправляем данные для изменения Имени")
    def test_updated_login_profile(self):
        new_token = self.get_token()
        response = requests.patch(Constants.URL + Constants.END_POINT_UPDATE_USER,
                                  headers={'Authorization': new_token}, data=DataForTest.data_double)

        assert response.status_code == 200 and response.json()['user']['name'] == 'Oleg'

    @allure.story("В этом тесте мы проверяем попытку обновления данных юзера без авторзации")
    @allure.title('Проверка авторизации в системе с валидными и невалидными данными')
    @allure.description("В этом тесте мы отправляем обновление данных юзера. Меняем имя.")
    @allure.tag("NewAPI", "Essentials", "UpdateUser")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://stellarburgers.nomoreparties.site", name="Website")
    @allure.issue("UpdateUser-06")
    @allure.testcase("TMS-06")
    @allure.step("Отправка PATCH запроса - с измененными данными без авторизации")
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_double, 400)
        )
    ])
    def test_create_user_fail(self, data, status_code):
        response = requests.patch(Constants.URL + Constants.END_POINT_UPDATE_USER,
                                  headers=Constants.headers, data=DataForTest.data_double, json=data)
        assert response.status_code == status_code
