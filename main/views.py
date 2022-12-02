from flask import render_template, request, Blueprint, redirect
from main.posts_dao import PostsDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates')
posts = PostsDAO('./data/posts.json', './data/comments.json')


@main_blueprint.route('/')
def index_page():
    """
    Главная страница по '/', в шаблон передаётся index.html
    """
    all_posts = posts.get_posts_all()
    return render_template('index.html', posts=all_posts)


@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    """
    Переход к посту по id, результат отправляем в шаблон post.html
    """
    # загрузили все посты
    found_post = posts.get_post_by_pk(postid)
    # проверили все комментарии с id
    comments = posts.get_comments_by_post_id(postid)
    return render_template('post.html', post=found_post, comments=comments)


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    """
    Поиск по вхождению ключевого слова
    """
    # передаём аргумент
    words = request.args.get('s')
    # получаем посты по определённому слову
    found_posts = posts.search_for_posts(words)
    return render_template('search.html', posts=found_posts)


@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page(username):
    """
    Поиск по имени
    """
    # передаём имя пользователя и перебираем посты
    user_posts = posts.get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts, username=username)
