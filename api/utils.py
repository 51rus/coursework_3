import json


def load_posts():
    """
    Загружает посты
    """
    with open('./data/posts.json', 'r', encoding='utf-8') as file:
        posts_data = json.load(file)
        return posts_data


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору
    """
    posts = load_posts()
    for post in posts:
        if post['pk'] == pk:
            return post
    return f'Такой пост не найден'
