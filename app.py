import logging

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import redirect

from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user, \
    bookmarks, bookmarks_add_post, bookmarks_del_post

# Импортируем блюпринт из пакета
from api.view_api import api_blueprint

# Создаем новый логгер
logger = logging.getLogger()

# Cоздаем ему обработчик
file_handler = logging.StreamHandler()

# Добавляем обработчик к журналу
logger.addHandler(file_handler)

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
# Регистрируем блюпринт api
app.register_blueprint(api_blueprint)


@app.route('/')
def catalog_page():
    posts = get_posts_all()
    count_bookmarks = len(bookmarks())
    return render_template("index.html", posts=posts, count_bookmarks=count_bookmarks)


@app.route('/posts/<int:postid>')
def post_full(postid):
    post = get_post_by_pk(postid - 1)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', comments=comments, post=post, postid=postid, count_comments=len(comments))


@app.route('/search/')
def search():
    search_word = request.values["s"]
    posts = search_for_posts(search_word)
    count_posts = len(posts)
    return render_template("search.html", posts=posts, count_posts=count_posts, search_word=search_word)


@app.route('/users/<username>')
def user_post(username):
    posts_by_user = get_posts_by_user(username)
    return render_template('user-feed.html', posts_by_user=posts_by_user, user_name=username)


@app.route('/bookmarks')
def bookmarks_view():
    bookmarks_list = bookmarks()
    return render_template('bookmarks.html', bookmarks_list=bookmarks_list)


@app.route('/bookmarks/add/<int:post_id>')
def bookmarks_add(post_id):
    bookmarks_add_post(post_id)
    return redirect("/", code=302)


@app.route('/bookmarks/remove/<int:post_id>')
def bookmarks_del(post_id):
    bookmarks_del_post(post_id)
    return redirect("/", code=302)


@app.errorhandler(500)
def error_server(e):
    return "<p>статус-код ошибки 500</p>", e


@app.errorhandler(404)
def error_server(e):
    return "<p>статус-код ошибки 400</p>", e


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=4400)
