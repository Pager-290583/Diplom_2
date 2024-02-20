import allure
import pytest
import requests

from data_test.user_data import DataForTest
from data_test.constants import Constants

base_url = f'{Constants.URL}'
end_point_login_user = f'{Constants.END_POINT_LOGIN_USER}'
headers = {"Content-Type": "application/json"}


@allure.epic("Логин пользователя")
@allure.feature("Авторизация пользователя")
class TestLoginUser:

    @allure.story("POST запрос - Авторизация пользователя в системе")
    @allure.title('Проверка авторизации в системе с валидными и невалидными данными')
    @allure.description("В этом тесте проверяются валидные данные для авторизации. Авторизация возможна"
                        "с корректными данными. Система возвращает корректныq стаус код")
    @allure.tag("NewAPI", "Essentials", "LoginCourier")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("LoginUser-03")
    @allure.testcase("TMS-03")
    @allure.step("Отправка POST запроса - с валидными данными")
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_double, 200)
        )
    ])
    def test_login_user_correct(self, data, status_code):
        response = requests.post(base_url + end_point_login_user, headers=headers, json=data).json()
        assert response['success'] == True


@allure.epic("Логин пользователя")
@allure.feature("Логин с неверным логином и паролем")
class TestLoginUser_2:
    @allure.story("POST запрос - логин с неверным логином и паролем")
    @allure.title('Проверка авторизации в системе с валидными и невалидными данными')
    @allure.description("В этом тесте проверяются логин с неверным логином и паролем")
    @allure.tag("NewAPI", "Essentials", "LoginCourier")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://qa-scooter.praktikum-services.ru", name="Website")
    @allure.issue("LoginCourier-04")
    @allure.testcase("TMS-04")
    @allure.step("Отправка POST запроса - с не валидными данными")
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_login_fail, 400)
        )
        ])
    def test_login_user_fail(self, data, status_code):
        response = requests.post(base_url + end_point_login_user, headers=headers, json=data).json()
        assert response['message'] == "email or password are incorrect"

