#!/usr/bin/env python3

from author import Author
from magazine import Magazine
from article import Article

if __name__ == "__main__":
    author1 = Author("Ernest Munyoki")
    author2 = Author("Jane Doe")
    author3 = Author("John Smith")

    mag1 = Magazine("TechLife", "Technology")
    mag2 = Magazine("HealthToday", "Health")
    mag3 = Magazine("ArtWorld", "Art")

    art1 = author1.add_article(mag1, "The Future of AI in Daily Life")
    art2 = author1.add_article(mag2, "5 Healthy Habits for Coders")
    art3 = author2.add_article(mag1, "Why Python is Taking Over the World")
    art4 = author2.add_article(mag1, "Understanding Cloud Computing")
    art5 = author2.add_article(mag1, "Top 10 Coding Best Practices")
    art6 = author3.add_article(mag3, "The Beauty of Abstract Art")

    print("Articles by Ernest:", [a.title for a in author1.articles()])
    print("Magazines Ernest has written for:", [m.name for m in author1.magazines()])
    print("Topics Ernest covers:", author1.topic_areas())

    print("\nArticles in TechLife:", [a.title for a in mag1.articles()])
    print("Contributors to TechLife:", [a.name for a in mag1.contributors()])
    print("Article titles in HealthToday:", mag2.article_titles())
    print("Frequent contributors in TechLife:", [a.name for a in mag1.contributing_authors()])

    print("\nAll Articles:", [a.title for a in Article.all()])
    print("All Magazines:", [m.name for m in Magazine.all()])
    print("Top Publisher:", Magazine.top_publisher().name)
