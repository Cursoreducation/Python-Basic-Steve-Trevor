def hello(func):
    def inner():
        print("Something is happening before func() is called")
        func()
        print("Something is happening after func() was called")

    return inner


@hello
def greetings():
    print('Hi there!')


# greetings = decorator(greetings)
greetings()
