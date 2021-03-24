import unittest
from ex1 import Calc
from ex1 import __version__ as v


class TestCalc(unittest.TestCase):
    @unittest.skipIf(v == "1.0.0", "skip if test")
    def test_sum(self):
        params = [
            [1, 2, 3],
            [2, 2, 4],
            [1, -2, -1],
            [-1, 2, 1],
            ["1", "1", 2],
            ["1", 1, 2],
            ["-1", 1, 0]
        ]
        for a, b, c in params:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(Calc.sum(a, b), c)

        with self.assertRaises(ValueError):
            Calc.sum("h", "1")

        with self.assertRaises(TypeError):
            Calc.sum([1], "1")

        self.assertIsInstance(Calc.sum(1, 1), float)

    # @unittest.skip("test")
    def test_minus(self):
        params = [
            [1, 2, -1],
            [2, 2, 0],
            [1, -2, 3],
            [-1, 2, -3],
            [-1, -2, 1],
            ["1", "1", 0],
            ["1", 1, 0],
            ["-1", 1, -2],
        ]
        for a, b, c in params:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(Calc.minus(a, b), c)

        with self.assertRaises(ValueError):
            Calc.sum("h", "1")

        with self.assertRaises(TypeError):
            Calc.sum([1], "1")

        self.assertIsInstance(Calc.sum(1, 1), float)

    def test_division(self):
        params = [
            [1, 2, 0.5],
            [2, 2, 1],
            [1, -2, -0.5],
            [-1, 2, -0.5],
            [-1, -2, 0.5],
        ]
        for a, b, c in params:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(Calc.division(a, b), c)

        self.assertIsInstance(Calc.division(1, 1), float)
        self.assertIsInstance(Calc.division(0.5, 0.5), float)
        self.assertIsInstance(Calc.division(0.5, -0.5), float)

        with self.assertRaises(ZeroDivisionError):
            Calc.division(1, 0)

    def test_mul(self):
        params = [
            [1, 2, 2],
            [2, 2, 4],
            [1, -2, -2],
            [-1, 2, -2],
            [-1, -2, 2],
        ]
        self.__repeat_assert_equal(params, Calc.mul)

        self.assertIsInstance(Calc.mul(1, 1), int)
        self.assertIsInstance(Calc.mul(0.5, 0.5), float)
        self.assertIsInstance(Calc.mul(0.5, -0.5), float)
        self.assertIsInstance(Calc.mul(1.0, 1), float)
        self.assertIsInstance(Calc.mul(1.0, 1.0), float)
        self.assertIsInstance(Calc.mul(0.5, 1.0), float)

    def __repeat_assert_equal(self, params, func):
        for a, b, c in params:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(func(a, b), c)

