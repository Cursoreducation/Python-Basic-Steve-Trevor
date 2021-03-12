# Single responsibility principle
class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass

    def save(self, user):
        pass

    def get_user(self, user_id):
        pass


# ------

class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass


class UserDB:
    def get_user(self, user_id):
        pass

    def save(self, user):
        pass


# Open/closed principle

# Bad practice
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favorite':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
        if self.customer == 'my_wife':
            return self.price * 0


# Best practice
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favorite':
            return self.price * 0.2


class VIPDiscount(Discount):
    def give_discount(self):
        return super().give_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    def give_discount(self):
        return super().give_discount() * 2


# Liskov substitution principle
class Board:
    def __init__(self, board_type):
        self.board_type = board_type

    def get_board_type(self):
        return self.board_type


class UserLiskov:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def move(self, piece, position):
        piece.move(position)


class OldBoard(Board):
    pass


board = Board('classic')
board_1 = OldBoard('Old classic')

user_white = UserLiskov('white', board)
user_black = UserLiskov('black', board_1)

# Interface segregation principle
from abc import ABC, abstractmethod


class Shape(ABC):
    # Best practice
    @abstractmethod
    def draw(self):
        raise NotImplementedError

    # Bad practice
    # def print(self):
    #     raise NotImplementedError


class Circle(Shape):
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        pass


# Dependency inversion principle

class AuthForUser:
    def __init__(self, connect):
        self.connect = connect

    def auth(self, credentials):
        pass

    def is_auth(self):
        pass

    def last_login(self):
        pass


class AnonAuth(AuthForUser):
    pass


class GitHubAuth(AuthForUser):
    def last_login(self):
        pass


class Permission(AuthForUser):
    def __init__(self, auth):
        self.auth = auth

    def has_persmission(self):
        pass


class IsLoggedInPermission(Permission):
    def last_login(self):
        return auth.last_login
