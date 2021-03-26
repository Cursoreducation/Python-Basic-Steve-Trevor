import logging
import time

time.asctime()

log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s'


logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="w", format=log_template)

name = "Misha"
logging.debug("debug")
logging.info(f"user {name} register item")
logging.debug("debug1")
logging.debug("debug2")
logging.warning("warning22")
logging.warning("warning")
logging.error("error")
logging.critical("critical1")
logging.critical("critical2")


a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError as er:
    logging.error("ZeroDivisionError", exc_info=True)