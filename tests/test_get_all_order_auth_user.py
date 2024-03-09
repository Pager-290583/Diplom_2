import allure
import pytest
import json
import requests
from data_test.constants import Constants
from data_test.user_data import DataForTest


@allure.epic("Получение заказов конкретного пользователя")
@allure.feature("Получаем заказы авторизованного и не авторизованного пользователя")
class TestGetOrderUser:
    @allure.story("Запрос всех заказаов конкретного пользователя по токену")
    @allure.title('Проверяем ответ системы авторизованного пользователя о его заказах')
    @allure.description("В этом тесте мы проверяем что имея авторизационный токен, "
                        "мы можем получить список заказов пользователя")
    @allure.tag("NewAPI", "Essentials", "GetOrder")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://stellarburgers.nomoreparties.site", name="Website")
    @allure.issue("UpdateUser-07")
    @allure.testcase("TMS-07")
    @allure.step("Получаем авторизационный токен и записываем его в переменную")
    def get_token(self):
        token = requests.post(Constants.URL + Constants.END_POINT_LOGIN_USER, headers=Constants.headers,
                              data=json.dumps(DataForTest.data_user))
        new_token = token.json()['accessToken']
        return new_token

    @allure.story("Запрос на получение заказов авторизованного пользователя")
    def test_get_order_login_user(self):
        new_token = self.get_token()
        response = requests.get(Constants.URL + Constants.END_POINT_ORDER,
                                headers={'Authorization': new_token}, data=DataForTest.updated_profile)
        body = response
        assert response.status_code == 200 and body.json()['success'] == True

    @allure.story("Запрос на получение заказов неавторизованного пользователя")
    def test_updated_order_not_login_user(self):
        response = requests.get(Constants.URL + Constants.END_POINT_ORDER, headers=Constants.headers)
        body = response
        assert response.status_code == 401 and body.json()['success'] == False
