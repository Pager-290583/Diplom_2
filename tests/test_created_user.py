import allure
import pytest
import requests

from data_test.user_data import DataForTest
from data_test.constants import Constants

base_url = f'{Constants.URL}'
end_point_creat_user = f'{Constants.END_POINT_CREAT_USER}'
headers = {"Content-Type": "application/json"}


class TestCreateCourier:

    @pytest.mark.parametrize(("data", "status_code"), [
        (
                pytest.param(DataForTest.data_200, 200)
        )
    ])
    def test_create_courier(self, data, status_code):
        response = requests.post(base_url + end_point_creat_user, headers=headers, json=data).json()
        assert status_code == 200 and response['success'] == True

    @pytest.mark.parametrize(("data", "status_code", "json"), [
        (
                pytest.param(DataForTest.data_403, 403,
                             {"success": False, "message": "User already exists"})
        ),
        (
                pytest.param(DataForTest.data_404, 403,
                             {"success": False, "message": "Email, password and name are required fields"})
        )
    ])
    def test_create_courier_fail(self, data, status_code, json):
        response = requests.post(base_url + end_point_creat_user, headers=headers, json=data)
        assert response.status_code == status_code
        assert response.json() == json
