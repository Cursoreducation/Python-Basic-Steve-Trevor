import unittest
import logging

from ex2 import Vector3f


class TestVector3f(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logging.basicConfig(level=logging.INFO, filename="test_vector3f.log", filemode="w")
        logging.info("Start test TestVector3f")

    @classmethod
    def tearDownClass(cls) -> None:
        logging.info("Finish test TestVector3f")

    def setUp(self) -> None:
        self.V1 = Vector3f(1, 2, 3)
        self.V2 = Vector3f(3, 2, 3)
        self.V3 = Vector3f(3.0, 2, 3)
        self.V4 = Vector3f(3, "2", 6)
        self.V5 = Vector3f("3", "2.0", 6)
        self.vectors = [self.V1, self.V2, self.V3, self.V4, self.V5]

    def test_init(self):
        logging.info("run test test_init")

        with self.assertRaises(ValueError):
            Vector3f("as", 1, 2)

        for vector in self.vectors:
            try:
                self.assertIsInstance(vector.x, int)
            except AssertionError as er:
                logging.error(f"x {vector.x} is not int in vector {vector}")
                raise er
            self.assertIsInstance(vector.y, float)
            self.assertIsInstance(vector.z, float)

    def test_str(self):
        self.assertEqual(str(self.V1), "(1.0, 2.0, 3.0)")

    def test_add(self):
        temp_vector = self.V1 + self.V2
        self.assertIsInstance(temp_vector, Vector3f)
        self.assertEqual(str(temp_vector), "(4.0, 4.0, 6.0)")
        self.V1 + 2
        self.assertEqual(str(self.V1), "(3.0, 4.0, 5.0)")

    def test_mul(self):
        self.assertEqual(self.V1 * self.V2, 16)
        self.assertIsInstance(self.V1 * self.V2, float)

        self.V3 * 2
        self.assertEqual(str(self.V3), "(6.0, 4.0, 6.0)")

    def test_module(self):
        self.assertEqual(self.V1.module(), 3.7416573867739413)
        self.assertIsInstance(self.V1.module(), float)

    def tearDown(self) -> None:
        print("tearDown")
