
class MyException(Exception):
    def __init__(self, txt, *args):
        self.txt = txt
        self.args = args


# raise MyException("error", 1, 1, 1, 1)

raise Exception("error", 1, 1, 1, 1)