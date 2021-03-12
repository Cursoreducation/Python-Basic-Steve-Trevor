def simple_generator(value):
    while value > 0:
        value -= 1
        yield 1


gen_iter = simple_generator(5)

# print(next(gen_iter))
# print('Hello')
# print(next(gen_iter))
# print('Hello')
# print(next(gen_iter))
# print('Hello')
# print('Hello')
# print('Hello')
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))

import random


def random_increase_number(quantity):
    num = 0
    while quantity > 0:
        num += random.random()
        quantity -= 1
        yield round(num, 2)


# generator = random_increase_number(5)
# for i in generator:
#     print(i)

gen = (round(random.random() + i, 2) for i in range(5))
print(next(gen))

# for i in gen:
#     print(i)
import os


def read_lines(directory, pattern=None):
    lines = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in file_names:
            if file_name.endswith('.py'):
                for line in open(os.path.join(dir_path, file_name)):
                    if pattern in line:
                        lines.append(line)
    yield lines
