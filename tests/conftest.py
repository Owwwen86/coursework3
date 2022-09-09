import pytest


@pytest.fixture()
def check_keys_post():
    return (
        "content", "poster_name", "poster_avatar", "pic", "views_count", "likes_count", "pk"
    )
