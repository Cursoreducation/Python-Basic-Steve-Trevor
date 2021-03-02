class Person:
    __slots__ = ('name', 'age')


anna = Person()
setattr(anna, 'name', 'Anna')
setattr(anna, 'person_id', 12345)
anna.name = 'Anna'
anna.age = 21
anna.person_id = 123456

print(anna.name)
print(anna.age)
print(anna.person_id)

print(anna.__dict__)
