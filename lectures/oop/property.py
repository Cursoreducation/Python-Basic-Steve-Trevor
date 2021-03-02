class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.14 * self.r ** 2


circle = Circle(10)
print(circle.area)

class Person:
    def __init__(self, name='Anna', age=0):
        self.name = name
        self._age = age

    @property
    def age(self):
        print('getter method called')
        return self._age

    # def get_age(self):
    #     return self._age

    @age.setter
    def age(self, x):
        if x < 18:
            print('setter method called')
            return False
        else:
            print('setter method called')
            self._age = x



    # def del_age(self):
    #     del self._age

    # age = property(get_age, set_age, del_age)


anna = Person()
anna.age = 16
print(anna.age)
