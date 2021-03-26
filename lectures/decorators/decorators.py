# def foo(bar):
#     return bar + 1
#
#
# print(foo)
# print(foo(2))
# print(type(foo))


def parent():
    print('Printing from the parent function')

    def first_child(a):
        return a + 2

    def second_child():
        return 'Printing from the second child'

    print(first_child(5))
    print(first_child(6))
    print(second_child())

parent()
