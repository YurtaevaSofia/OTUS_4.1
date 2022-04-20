from requests import get


def test_codes(url, code):
    target = url
    response = get(url=target)
    assert response.status_code == int(code)

