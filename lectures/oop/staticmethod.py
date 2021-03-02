def is_adult(age):
    if age > 18:
        return True
    else:
        return False


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False


anna = Person('Anna', 21)
print(is_adult(21))
