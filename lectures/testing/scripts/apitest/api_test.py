import unittest
import requests
from apitest.exceptions import *
from apitest.api_script import Register


class TestRegisterApi(unittest.TestCase):
    def setUp(self) -> None:
        self.debug_server = Register()

    def test_get(self):
        response = requests.get("http://127.0.0.1:5000/register")
        self.assertEqual(response.status_code, 200)

        response = requests.get("http://127.0.0.1:5000/registe")
        self.assertEqual(response.status_code, 404)

    def test_psw_len(self):
        data = {
            "name": "Misha",
            "psw": "qwert",
        }
        with self.assertRaises(PswLenError):
            response = self.debug_server.get(data)

    def test_psw_symbols(self):
        data = {
            "name": "Misha",
            "psw": "qwert!)(",
        }

        with self.assertRaises(PswWrongSymbolsError):
            response = self.debug_server.get(data)

    def test_name_symbols(self):
        data = {
            "name": "Misha()",
            "psw": "qwertyy",
        }

        with self.assertRaises(NameWrongSymbolsError):
            response = self.debug_server.get(data)

    def test_name_len(self):
        data = {
            "name": "M",
            "psw": "qwertyy",
        }
        with self.assertRaises(NameLenError):
            response = self.debug_server.get(data)
