import json

POST_PATH = "data/posts.json"
COMMENT_PATH = 'data/comments.json'
BOOKMARK_PATH = "data/bookmarks.json"


def get_posts_all() -> list[dict]:
    """ Возвращает посты """
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name) -> list[dict]:
    """ Возвращает посты определенного пользователя. Функция вызывает ошибку `ValueError`
     если такого пользователя нет и пустой список, если у пользователя нет постов.

    """

    posts_by_user = []
    count_posts = 0
    for post in get_posts_all():
        if user_name == post['poster_name']:
            count_posts += 1
            posts_by_user.append(post)
    if count_posts == 0:
        raise ValueError('Нет такого пользователя')
    return posts_by_user


def get_comments_by_post_id(post_id):
    """ Возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError`
    если такого поста нет и пустой список, если у поста нет комментов.

    """
    comment_list = []
    post_is_true = False
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == post_id:
            post_is_true = True
            break
    if post_is_true:
        with open(COMMENT_PATH, 'r', encoding='utf-8') as file:
            comment_data = json.load(file)
            for comment in comment_data:
                if comment['post_id'] == post_id:
                    comment_list.append(comment)
        return comment_list
    else:
        raise ValueError('Нет такого поста')


def search_for_posts(query):
    """ Возвращает список постов по ключевому слову """
    search_post = []
    all_posts = get_posts_all()
    for post in all_posts:
        if query in post['content']:
            search_post.append(post)
    return search_post


def get_post_by_pk(pk):
    """ Возвращает один пост по его идентификатору """
    post = get_posts_all()
    return post[pk]


def bookmarks():
    """ Открывает bookmarks.json """
    with open(BOOKMARK_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def bookmarks_add_post(post_id) -> dict:
    """ Записывает данные в bookmarks.json """
    posts = get_posts_all()
    bookmarks_list = bookmarks()
    for post in posts:
        if post['pk'] == post_id:
            bookmarks_list.append(post)
            break
    with open(BOOKMARK_PATH, 'w', encoding='utf-8') as file:
        json.dump(bookmarks_list, file, ensure_ascii=False)


def bookmarks_del_post(post_id) -> dict:
    """ Удаляет запись из bookmarks.json """
    posts = get_posts_all()
    bookmarks_list = bookmarks()
    for bookmark in bookmarks_list:
        if bookmark['pk'] == post_id:
            bookmarks_list.remove(bookmark)
            break
    with open(BOOKMARK_PATH, 'w', encoding='utf-8') as file:
        json.dump(bookmarks_list, file, ensure_ascii=False)
