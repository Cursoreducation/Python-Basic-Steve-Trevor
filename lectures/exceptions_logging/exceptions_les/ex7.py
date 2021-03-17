import requests
from requests import HTTPError, ConnectionError


try:
    r = requests.get("https://www.google.com.ua/")
except HTTPError:
    pass

