import pytest

POSTS_MAX = 200

from Homework12.test.conftest import ApiTestCase
from unittest.mock import Mock
import requests

# создание заглушки для ответа сервера
response = Mock()
response.status_code = 200
response.json.return_value = {
    'id': POSTS_MAX
}
# настоящий объект тест-кейса
api_test = ApiTestCase("0.0.0.0", requests.Session())
# создание заглушки для GET-запроса
api_test.get = Mock(return_value=response)

"""
_______________________________________________________________
a) positive/negative тесты для Getting a resource
---------------------------------------------------------------
"""
@pytest.mark.parametrize('id', [POSTS_MAX])
def test_get_positive(api_test, id):
    res = api_test.get(id)
    assert res.status_code == 200
    assert res.json()['id'] == id

"""
_______________________________________________________________
c) positive тесты для Creating a resource
---------------------------------------------------------------
"""
response.json.return_value = {
    'id': POSTS_MAX + 1,
    'userId':  1,
    'title': 'foo',
    'body': 'bar'
}
# создание заглушки для POST-запроса
api_test.post = Mock(return_value=response)

@pytest.mark.parametrize("userId", [1])
@pytest.mark.parametrize("title, body", [('foo', 'bar')])
def test_create_positive(api_test, userId, title, body):
    payload = {'title': title, 'body': body, 'userId': userId}
    res = api_test.post(payload)
    j = res.json()
    assert j['id'] == POSTS_MAX + 1
    assert j['userId'] == userId
    assert j['title'] == title
    assert j['body'] == body


