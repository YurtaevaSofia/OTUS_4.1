import pytest
from requests import get, post, put, delete
import cerberus

base_url = "https://jsonplaceholder.typicode.com/"


def test_get_post():
    target = base_url + "posts/1"
    responce = get(url=target)
    assert responce.status_code == 200


def test_post_schema():
    target = base_url + "posts/1"
    response = get(url=target)
    schema = {
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'},
        'userId': {'type': 'number'}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)


def test_create_post():
    target = base_url + "posts"
    body = {
        'title': 'title1',
        'body': 'body1',
        'userId': 1
    }
    response = post(url=target, data=body)
    schema = {
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'},
        'userId': {'type': 'string'}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)


def test_create_update():
    target = base_url + "posts"
    body = {
        'title': 'title1',
        'body': 'body1',
        'userId': 1
    }
    response = post(url=target, data=body)
    id_from_json = response.json()['id']
    new_target = base_url + "posts/" + str(id_from_json)
    print(new_target)
    new_body = {
        'id': 1,
        'title': 'title2',
        'body': 'body2',
        'userId': 1
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    new_response = put(url=new_target, data=new_body, headers=headers)
    assert new_response.json()['title'] == 'title2'


def test_create_delete():
    target = base_url + "posts"
    body = {
        'title': 'title1',
        'body': 'body1',
        'userId': 1
    }
    response = post(url=target, data=body)
    id_from_json = response.json()['id']
    new_target = base_url + "posts/" + str(id_from_json)
    new_response = delete(url=new_target)
    assert new_response.status_code == 200
