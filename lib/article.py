class Article:
    all = []

    def __init__(self, author, magazine, title):
        from .author import author
        from .magazine import Magazine

        if not isinstace(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstace(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <=50):
            raise Exception("Title must be a string between 5 and 50 chars")

        self.author = author 
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        self._magazine = value
