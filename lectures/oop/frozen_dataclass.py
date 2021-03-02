import dataclasses


@dataclasses.dataclass(frozen=True)
class Book:
    title: str
    author: str
    pages: int
    rate: float


it = Book(title='IT', author='Stephan King', pages=1205, rate=4.58)

print(f"I read the {it.title} of {it.author}, it has {it.pages} pages and rate {it.rate}")

