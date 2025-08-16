from article import Article
from author import Author

class Magazine:
    _all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Magazine category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article.all() if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        frequent = [author for author in set(authors) if authors.count(author) > 2]
        return frequent if frequent else None

    @classmethod
    def top_publisher(cls):
        if not Article.all():
            return None
        return max(cls._all, key=lambda mag: len(mag.articles()))

    @classmethod
    def all(cls):
        return cls._all

