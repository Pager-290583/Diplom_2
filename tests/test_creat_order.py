import allure
import requests
import pytest

from data_test.user_data import DataForTest
from data_test.constants import Constants


@allure.epic("Создание заказа")
@allure.feature("Создание заказа без авторзации")
class TestCreateOrder:
    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_ingridient, 200)
        )
    ])
    @allure.step("Создания заказа без авторизации с ингредиентами")
    def test_create_order_01(self, data, status_code):
        response = requests.post(Constants.URL + Constants.END_POINT_ORDER, headers=Constants.headers,
                                 json=data).json()
        assert (status_code == 200 and response['success'] == True
                and response['name'] == "Бессмертный флюоресцентный бургер")

    @pytest.mark.parametrize("data", [
        (
                pytest.param(DataForTest.data_not_ingridient)
        )
    ])
    @allure.step("Создания заказа без авторизации без ингредиентов")
    def test_create_order_02(self, data):
        response = requests.post(Constants.URL + Constants.END_POINT_CREAT_ORDER, headers=Constants.headers,
                                 json=data)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @pytest.mark.parametrize("data", [
        (
                pytest.param(DataForTest.data_bad_ingridient)
        )
    ])
    @allure.step("Создания заказа без авторизации с неверным хешем ингредиентов")
    def test_create_order_03(self, data):
        response = requests.post(Constants.URL + Constants.END_POINT_CREAT_ORDER, headers=Constants.headers,
                                 json=data)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"One or more ids provided are incorrect"}'