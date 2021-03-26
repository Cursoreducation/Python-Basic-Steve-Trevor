def smart_divide(func):
    def inner(a, b):
        print(f'I am going to divide {a} and {b}')
        if b == 0:
            print('Oop! Cannot divide')
            return
        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


# divide(6, 0)

def tags(tag_name):
    def tags_decorator(func):
        def inner(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        return inner

    return tags_decorator


def tags_decorator_with_div(func):
    def inner(name):
        return "<{0}>{1}</{0}>".format('div', func(name))

    return inner


@tags("div")
def get_text(name):
    return 'Hello ' + name


print(get_text('Anna'))
