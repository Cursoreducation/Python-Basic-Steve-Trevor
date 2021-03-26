__version__ = "1.0.1"


class Calc:
    @staticmethod
    def sum(a, b):
        """
        >>> Calc.sum(1, 2)  # doctest: +SKIP
        3
        >>> Calc.sum(2, 2)
        4
        >>> Calc.sum(1, 1)
        2

        :param a:
        :param b:
        :return:
        """
        a = float(a)
        b = float(b)

        return a + b

    @staticmethod
    def minus(a, b):
        """
        >>> Calc.minus(1, 1)
        0

        :param a:
        :param b:
        :return:
        """
        a = float(a)
        b = float(b)

        return a - b

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def mul(a, b):
        return a * b



