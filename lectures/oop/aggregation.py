class Book:
    def __init__(self):
        page_1 = Page('This is content of page 1')
        page_2 = Page('This is content of page 2')
        self.pages = [page_1, page_2]


class Page:
    def __init__(self, content):
        self.content = content

book = Book()