from .article import Article

class Author:
    def init__(self,name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be a non-empty string.")
            self.name = name

@property
def name(self):
    return self._name

def articles(self):
    return [articles for articles in Article.all() if articles.author == self]

def magazines(self):
    return list({article.magazine for article in self.articles()})

def add_article(self, magazine, title):
    from .magazine import Magazine 
    if not isinstance(magazine, Magazine):
        raise Exception("Must provide a Magazine instace.")
        return Article(magazine, self, title)

def topic_areas(self):
    if len(self.articles()) == 0:
        return none
        return list({magazine.category for magazine in self.magazines()})