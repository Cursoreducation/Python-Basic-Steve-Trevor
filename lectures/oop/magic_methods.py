a = 'str'
print(dir(a))

class Student:
    def __init__(self, student_id, rate):
        self.student_id = student_id
        self.rate = rate

    def __new__(cls, student_id, rate):
        print('Creating the instance')
        instance = super(Student, cls).__new__(cls)
        if rate > 5:
            return instance
        else:
            print('Your rete is too low.')

    def __str__(self):
        return 'Hello'

student = Student(1234, 4)
print(student)

class CallArea:
    def __call__(self, a, b, c):
        p = a + b + c / 2
        return (p * 2) / 3

area = CallArea()
print(area(3, 4, 5))

class Count:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count < 5:
            total_count = self.count + other.count
        else:
            total_count = self.count + (other.count * 2)
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'


c1 = Count(3)
c2 = Count(8)
c3 = c1 + c2
print(c3)

class MyClass:
    def __init__(self):
        print('Instance created')

    def __call__(self):
        print('Instance is called via __call__')

key = MyClass()

key()