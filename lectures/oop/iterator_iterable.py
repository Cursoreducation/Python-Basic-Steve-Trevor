# a = {1: 'a', 2: 'b'}
# c = [1, 2, 3, 4, 5, 6]
# b = iter(a)
# d = iter(c)
# next(d)
# print(b)
# # print(next(b))
# # print(next(b))
# # print(next(b))
# for k in a:
#     print(k)
import random


class RandomIncreaseNumber:
    def __init__(self, quantity):
        self.qty = quantity
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.num += random.random()
            self.qty -= 1
            return round(self.num, 3)
        else:
            raise StopIteration


iterator = RandomIncreaseNumber(10)
for i in iterator:
    print(i)


# print(next(iterator))


def check_if_iterable(obj):
    return '__getitem__' in dir(obj)


types_to_check = [int, bool, str, set, frozenset, tuple, list, float, dict, complex, bytes,
                  bytearray]
for type_to_check in types_to_check:
    print(f"{type_to_check} Iterable {check_if_iterable(type_to_check)}")
