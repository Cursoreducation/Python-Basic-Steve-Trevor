import collections

Article = collections.namedtuple('Article', ['topic', 'author', 'language', 'likes', 'rate'])

python = Article('Python', 'John', 'EN', 2345, 4.25)

print(python[3])

print(python.rate)

python.reviewer = 'Anna'