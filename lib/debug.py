#!/usr/bin/env python3

from author import Author
from magazine import Magazine
from article import Article

# Create some authors
a1 = Author("Alice")
a2 = Author("Bob")

# Create some magazines
m1 = Magazine("TechWorld", "Technology")
m2 = Magazine("Foodie", "Cooking")

# Create articles
art1 = a1.add_article(m1, "The Future of AI")
art2 = a1.add_article(m2, "Best Pasta Recipes")
art3 = a2.add_article(m1, "Cloud Computing Basics")

print("Articles by Alice:", [a.title for a in a1.articles()])
print("Magazines Alice writes for:", [m.name for m in a1.magazines()])

print("Articles in TechWorld:", [a.title for a in m1.articles()])
print("Contributors to TechWorld:", [a.name for a in m1.contributors()])

print("Topic areas for Alice:", a1.topic_areas())
print("Article titles in Foodie:", m2.article_titles())

print("Top publisher:", Magazine.top_publisher().name if Magazine.top_publisher() else None)
