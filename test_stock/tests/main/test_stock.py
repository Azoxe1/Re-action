import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from main.models import UserInfo

@pytest.fixture
def user():
    return APIClient()

@pytest.fixture
def User_factory():
    def factory(*args, **kwargs):
        return baker.make(UserInfo, *args, **kwargs)
    return factory

@pytest.mark.django_db  #проверка, что генерируемые пользователи равны запрашиваемым
def test_course_filter(client, User_factory):
    users = User_factory(_quantity = 10)
    user_id = users[0].id
    response =  client.get(f'/users/{user_id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['user_name'] == users[0].user_name
