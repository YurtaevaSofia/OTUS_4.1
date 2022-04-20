import pytest
from requests import get
import cerberus

base_url = "https://dog.ceo/api/"


def test_list_of_breeds():
    target = base_url + "breeds/list/all"
    responce = get(url=target)
    assert responce.status_code == 200


def test_list_of_breeds_status():
    target = base_url + "breeds/list/all"
    response = get(url=target)
    assert response.json()['status'] == "success"


def test_list_of_breeds_schema():
    target = base_url + "breeds/list/all"
    response = get(url=target)
    schema = {
        'message': {'type': 'dict'},
        'status': {'type': 'string'}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)


def test_random_image():
    target = base_url + "breeds/image/random"
    responce = get(url=target)
    assert responce.status_code == 200


def test_list_of_random_image_status():
    target = base_url + "breeds/image/random"
    response = get(url=target)
    assert response.json()['status'] == "success"


def test_random_image_schema():
    target = base_url + "breeds/image/random"
    response = get(url=target)
    schema = {
        'message': {'type': 'string'},
        'status': {'type': 'string'}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)


@pytest.mark.parametrize('breed', ["hound", "affenpinscher", "husky", "maltese"])
def test_random_breed_image(breed):
    target = base_url + "breed/" + breed + "/images"
    responce = get(url=target)
    assert responce.status_code == 200


@pytest.mark.parametrize('breed', ["hound", "affenpinscher", "husky", "maltese"])
def test_list_of_random_image_status(breed):
    target = base_url + "breed/" + breed + "/images"
    response = get(url=target)
    assert response.json()['status'] == "success"