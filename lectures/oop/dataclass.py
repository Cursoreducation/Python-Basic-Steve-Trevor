import dataclasses


@dataclasses.dataclass
class Article:
    """
    This class for holding the article content information
    """
    topic: str
    author: str
    language: str
    likes: int
    rate: float


python = Article('Python', 'John', 'EN', 2345, 4.05)
python.reviewers = 'Anna'
print(type(python.topic))


print(python)
print(python.rate)

python_d = {'topic': 'Python', 'author': 'John', 'language': 'EN', 'likes': 2345, 'rate': 4.05}
print(python_d['likes'])