class Person:
    name = 'Anna'


anna = Person()

setattr(anna, 'name', 'John')
# print(anna.name)
print(getattr(anna, "name"))

setattr(anna, 'age', 21)
# print(anna.age)
print(getattr(anna, 'age'))

john = Person()
john.age