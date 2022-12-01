from api.utils import load_posts, get_post_by_pk


def test_load_posts():
    """
    Проверка на тип полученного значения на список (list)
    """
    assert type(load_posts()) == list


expected_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']


def test_keys_in_load_posts():
    """
    Проверка наличия у элементов нужных ключей
    """
    for post in load_posts():
        # Перебор списка из полученных постов
        keys = [key for key in post.keys()]
        assert keys == expected_keys


def test_get_post_by_pk():
    """
    Обратная проверка на тип полученного значения на словарь (dict)
    """
    for i in range(1, 8):
        assert type(get_post_by_pk(i)) == dict


def test_keys_in_get_post_by_bk():
    """
    Проверка наличия у элементов нужных ключей
    """
    for i in range(1, 8):
        # Перебор ключей из объекта
        keys = [key for key in get_post_by_pk(i).keys()]
        assert keys == expected_keys
