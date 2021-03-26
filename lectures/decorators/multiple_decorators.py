def uppercase(func):
    def inner():
        make_uppercase = func().upper()
        return make_uppercase

    return inner


def split_str(func):
    def inner():
        splitter_str = func().split()
        return splitter_str

    return inner


@split_str
@uppercase
def greetings():
    return 'hello there'


print(greetings())
