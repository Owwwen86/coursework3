import json

POST_PATH = "data/posts.json"


def get_posts_all() -> list[dict]:
    """ Возвращает посты """
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_post_by_pk(pk):
    """ Возвращает один пост по его идентификатору """
    post = get_posts_all()
    return post[pk]