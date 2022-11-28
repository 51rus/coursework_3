import json

from main.post import Post


class PostsDAO:
    """
    Обращение к данным поста, загрузка данных
    """

    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_posts(self):
        """
        Загружает посты
        """
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            # список постов, в которые будут добавляться полученные посты
            new_posts = []
            posts_data = json.load(file)

            for post in posts_data:
                new_posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']))
        return new_posts

    def load_comments(self):
        """
        Загружает комментарии
        """
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
        return comments

    def get_posts_all(self):
        """
        Вызывает функцию load_posts
        """
        return self.load_posts()

    def get_posts_by_user(self, user_name):
        """
        Возвращает посты по юзеру (поиск по имени)
        """
        posts = self.load_posts()
        # список для постов по имени
        user_posts = []

        for post in posts:
            if post.poster_name.lpwer() == user_name.lower():
                user_posts.append(post)
        return user_posts

    def get_comments_by_post_id(self, post_id):
        """
        Возвращает комментарии определенного поста (поиск по id)
        """
        comments = self.load_comments()
        # список для постов по id
        comments_posts = []

        for comment in comments:
            if comment['post_id'] == post_id:
                comments_posts.append(comment)
        return comments_posts

    def search_for_posts(self, query):
        """
        Возвращает список постов по ключевому слову
        """
        posts = self.load_posts()
        # список для постов по ключевому слову
        new_posts = []
        for post in posts:
            if query.lower() == post.content.lower():
                new_posts.append(post)
        return new_posts

    def get_post_by_pk(self, pk):
        """
        Возвращает один пост по его идентификатору
        """
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post
        # если пост не найден
        return None
