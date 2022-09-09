import logging

from flask import Blueprint, jsonify

from api.utils_api import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)

# Создаем новый логгер
api_logger = logging.getLogger(name=None)

# Cоздаем ему обработчик
file_handler = logging.FileHandler("../coursework2_source/logs/api.log")

# Создаем новое форматирование
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# Применяем форматирование к обработчику
file_handler.setFormatter(formatter_api)


@api_blueprint.route("/api/posts/")
def get_all_posts():
    api_logger.addHandler(file_handler)
    return jsonify(get_posts_all())


@api_blueprint.route("/api/posts/<int:post_id>")
def get_post(post_id):
    api_logger.addHandler(file_handler)
    return jsonify(get_post_by_pk(post_id-1))
