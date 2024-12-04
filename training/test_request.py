import requests


def test_simple_request():
    request = requests.get("https://x-clients-be.onrender.com/company")
    assert request.status_code == 200
    request.json()
