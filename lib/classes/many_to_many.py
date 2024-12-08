class Article:
    all = []  

    def __init__(self, author, magazine, title):
        
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self.title = title
        

        author._articles.append(self)
        magazine._articles.append(self)

        
        Article.all.append(self)

    def __repr__(self):
        return f"Article(title='{self.title}')"


class Author:
    def __init__(self, name):
    
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")

        self.name = name
        self._articles = [] 

    def articles(self):
        
        return self._articles

    def magazines(self):
        
        return list(set(article.magazine for article in self._articles)) if self._articles else []

    def add_article(self, magazine, title):
        
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        
        return list(set(magazine.category for magazine in self.magazines())) or None


class Magazine:
    _all_magazines = []  

    def __init__(self, name, category):

        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters")

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")

        self._name = name
        self._category = category
        self._articles = []  

        
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        
        return self._articles

    def contributors(self):
        
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        
        return [article.title for article in self._articles] or None

    def contributing_authors(self):
        
        authors = {}
        for article in self._articles:
            authors[article.author] = authors.get(article.author, 0) + 1
        return [author for author, count in authors.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        
        return max(cls._all_magazines, key=lambda mag: len(mag.articles()), default=None)
