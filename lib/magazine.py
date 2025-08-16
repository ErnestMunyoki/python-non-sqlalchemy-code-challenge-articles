from .article import Article

class Magazine:
    all = []

    def__init__(self, name, category):
        self.name = name 
        self.category = category
        Magazine.all.append(self)

@property
def name(self):
    return self._name

@name.setter 
def name(self, value):
    if not isinstance(value, str) or not (2 <= len(value) <= 16):
        raise Exception("Name must be a string between 2 and 16 chars")
    self._name = value

@property
def category(self):
    return self._category

@category.setter
def category(self, value):
   if not isinstance(value, str) or len(value.strip()) == 0:
       raise Exception("Category must be a non-empty string.")
   self._category = value

def articles(self):
    return [article for article in Article.all if article.magazine == self]

def contributors(self):
    return list({article.author for article in self.articles()})

def article_titles(self):
    titles = [article.title for article in self.articles()]
    return titles if titles else None

def contribuitng_authors(self):
    authors = [articles.author for articles in self.articles()]
    result = [author for author in set(authors) if authors.count(author) > 2]
    return result if result else None

@classmethod
def top_publisher(cls):
    if len(Article.all) == 0:
        return None
    return max(cls.all, key=lambda mag: len(mag.articles()))