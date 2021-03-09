vec_3f_1 = (1, 2, 3)
vec_3f_2 = (3, 2, 1)


"qwewqe {}".format(1)

f"{1}"

class Vec:
    def __init__(self, vec_3f):
        self.vec_3f = vec_3f
        self.__temp = vec_3f

    def __mul__(self, other):
        pass

    def __add__(self, other):
        pass

    def __enter__(self):
        return self.vec_3f

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.vec_3f = self.__temp

vector = Vec((1, 2, 3))

with vector as vector:
    vector *= 1
    vector += (1, 2)
