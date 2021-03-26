from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        """
        Logging
        :param args:
        :param kwargs:
        :return:
        """
        print(f'{func.__name__} was called')
        return func(*args, **kwargs)

    return with_logging


@logged
def greetings(name):
    """
    Greetings
    :param name:
    :return:
    """
    return f'Hi {name}!'

@logged
def f(x):
    """
    fdf
    :param x:
    :return:
    """
    return x


print(greetings.__name__)
print(greetings.__doc__)
print(f.__name__)
print(f.__doc__)
