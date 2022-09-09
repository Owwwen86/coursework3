import pytest

from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id


def test_get_post_all():
    list = []
    result = get_posts_all()
    assert type(result) == type(list), 'JSON файл не преобразован в список'


def test_get_posts_by_user():
    list = []
    result = get_posts_by_user('leo')
    assert type(result) == type(list), 'Данные не преобразованы в список'


def test_comments_by_post_id():
    list = []
    result = get_comments_by_post_id(2)
    assert type(result) == type(list), 'Данные не преобразованы в список'


def test_get_posts_by_user_val_error():
    with pytest.raises(ValueError):
        get_posts_by_user('vasya')


def test_get_comments_by_post_id():
    with pytest.raises(ValueError):
        get_comments_by_post_id(10)