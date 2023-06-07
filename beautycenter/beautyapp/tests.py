import requests


def test_home_page():
    url = 'http://127.0.0.1:8080/'
    response = requests.get(url)
    assert response.status_code == 200


def test_about_page():
    url = 'http://127.0.0.1:8080/services/'
    response = requests.get(url)
    assert response.status_code == 200


def test_film_page_1():
    url = 'http://127.0.0.1:8080/services/add/'
    response = requests.get(url)
    assert response.status_code == 200


def test_film_page2():
    url = 'http://127.0.0.1:8080/categories/'
    response = requests.get(url)
    assert response.status_code == 200


def test_film_page3():
    url = 'http://127.0.0.1:8080/categories/add/'
    response = requests.get(url)
    assert response.status_code == 404


def test_genre_page1():
    url = 'http://127.0.0.1:8080/clients/'
    response = requests.get(url)
    assert response.status_code == 200


def test_genre_page2():
    url = 'http://127.0.0.1:8080/doctors/'
    response = requests.get(url)
    assert response.status_code == 200


def test_genre_page3():
    url = 'http://127.0.0.1:8080/doctors/add/'
    response = requests.get(url)
    assert response.status_code == 404