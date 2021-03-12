from abc import ABC, abstractmethod


class Greetings(ABC):
    @abstractmethod
    def say_hello(self):
        raise NotImplementedError

    @abstractmethod
    def say_goodbye(self):
        pass


class Ukraine(Greetings):
    def say_hello(self):
        print('Привіт')

    def say_goodbye(self):
        print('Допобачення')

# a = Greetings()
# a.say_hello()
ukr = Ukraine()
ukr.say_hello()
ukr.say_goodbye()
