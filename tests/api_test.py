import pytest
from app import app


def test_all_posts():
    """ Функция проверяет, является ли списком данные получаемые по данному маршруту"""
    posts = []
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == type(posts)


def test_all_post_keys(check_keys_post):
    """ Функция проверяет наличие необходимых ключей в данных, получаемых по данному маршруту"""
    response = app.test_client().get('/api/posts/')
    flag = True
    for i in range(0, len(check_keys_post)):
        key = check_keys_post[i]
        for i in range(0, len(response.json)):
            if key not in response.json[i]:
                flag = False
                break
    assert flag == True


def test_posts_id():
    """ Функция проверяет, является ли словарем данные получаемые по данному маршруту"""
    posts = {}
    response = app.test_client().get('/api/posts/2')
    assert type(response.json) == type(posts)


def test_id_post_keys(check_keys_post):
    """ Функция проверяет наличие необходимых ключей в данных, получаемых по данному маршруту"""
    response = app.test_client().get('/api/posts/3')
    flag = True
    for i in range(0, len(check_keys_post)):
        key = check_keys_post[i]
        if key not in response.json:
            flag = False
            break
    assert flag == True
