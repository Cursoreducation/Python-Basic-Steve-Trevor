# Timer
import requests
import time
from functools import wraps


def benchmark(func):
    def inner(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Runtime: {end - start} sec')
        return return_value

    return inner


@benchmark
def fetch_webpage(url):
    web_page = requests.get(url)
    return web_page.text


# webpage = fetch_webpage('https://google.com')
# print(webpage)

# logging

import logging


def logger(func):
    # log = logging.getLogger(__name__)
    @wraps(func)
    def inner(a, b):
        print(f"Calling func: {func.__name__}")
        print(f'This func accepts such type of args: {type(a)}, {type(b)}')
        print(f'The docstring of this func is: {func.__doc__}')
        result = func(a, b)
        print(f'The call of the func is done.')
        return result

    return inner


@logger
def add(a, b):
    """
    Add the 2 numbers
    :param a: int
    :param b: int
    :return: int
    """
    print(f"Adding {a} + {b}")
    return a + b


# print(add(5, 3))
#
# print(add.__doc__)
# print(add.__name__)

# error handler


def error_handler(func):
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
        except ZeroDivisionError:
            print(f'Wrong result of func: {func.__name__}')
            add(*args, **kwargs)
        return result

    return wrapper


@error_handler
def divide(a, b):
    return a / b


# print(divide(5, 0))


# slow down
def slowdown(func):
    @wraps(func)
    def inner(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return inner


@slowdown
def countdown(number):
    if number < 1:
        print('Done')
    else:
        print(number)
        countdown(number - 1)


# countdown(10)


# debugging
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_reps = [repr(a) for a in args]
        kwargs_repo = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_reps + kwargs_repo)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result

    return wrapper


@debug
def greetings(name, age=None):
    if not age:
        return f"Hello {name}!"
    else:
        return f"Hello {name}! You are {age} years old"

greetings('Anna')

greetings('Rob', 25)