import allure
import pytest
import requests

from data_test.user_data import DataForTest
from data_test.constants import Constants


@allure.epic("Тестирование АПИ")
@allure.feature("Создание пользователя")
class TestCreateCourier:
    @allure.story("POST запрос на создать уникального пользователя")
    @allure.title('Тестирование валидации при создании нового пользователя в системе')
    @allure.description("В этом тесте проходит валидация статус кодов и тела ответа."
                        " Статус 201 success: True")
    @allure.tag("NewAPI", "Essentials", "CreatUser")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://stellarburgers.nomoreparties.site", name="Website")
    @allure.issue("CREAT-01")
    @allure.testcase("TMS-01")
    @allure.step("Отправка POST запроса с заголовком и данными нового пользователя")
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_200, 200)
        )
    ])
    def test_create_user(self, data, status_code):
        response = requests.post(Constants.URL + Constants.END_POINT_CREAT_USER, headers=Constants.headers,
                                 json=data).json()
        assert status_code == 200 and response['success'] == True

    @allure.story("POST запрос на создать пользователя, который уже зарегистрирован")
    @allure.title('Тестирование валидации при создании нового пользователя в системе')
    @allure.description("В этом тесте проходит валидация статус кодов и тела ответа."
                        " Статус 201 success: True")
    @allure.tag("NewAPI", "Essentials", "CreatUser")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Kozlov Oleg")
    @allure.link("https://stellarburgers.nomoreparties.site", name="Website")
    @allure.issue("CREAT-02")
    @allure.testcase("TMS-02")
    @allure.step("Отправка POST запроса для создания пользователя, который уже зарегистрирован")
    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(DataForTest.data_double, 403,
                             {"success": False, "message": "User already exists"})
        ),
        (
                pytest.param(DataForTest.data_404, 403,
                             {"success": False, "message": "Email, password and name are required fields"})
        )
    ])
    def test_create_user_fail(self, data, status_code, json):
        response = requests.post(Constants.URL + Constants.END_POINT_CREAT_USER, headers=Constants.headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json
