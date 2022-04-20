import pytest
from jsonschema import validate
from requests import get
import cerberus

base_url = "https://api.openbrewerydb.org/breweries"


def test_list_of_breweries():
    target = base_url
    responce = get(url=target)
    assert responce.status_code == 200


def test_list_of_breweries_schema():
    target = base_url
    response = get(url=target)
    schema = {
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'city': {'type': 'string'},
        'state': {'type': 'string'},
        'phone': {'type': 'number'},
        'website_url': {'type': 'string'}
    }
    validate(instance=response.json()[0], schema=schema)


@pytest.mark.parametrize('city', ["new_york", "san_diego", "chicago"])
def test_list_of_breweries_by_city(city):
    target = base_url + "?by_city=" + city
    response = get(url=target)
    assert response.status_code == 200


@pytest.mark.parametrize('look_for', ["dog", "cat", "humster"])
def test_list_of_breweries_by_part_name(look_for):
    target = base_url + "/search?query=" + look_for
    response = get(url=target)
    assert response.status_code == 200


@pytest.mark.parametrize('part_name', ["dog", "cat", "rat"])
def test_list_of_breweries_schema(part_name):
    target = base_url + "/autocomplete?query=" + part_name
    response = get(url=target)
    schema = {
        'id': {'type': 'string'},
        'name': {'type': 'string'}
    }
    validate(instance=response.json()[0], schema=schema)