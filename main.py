import os.path
import article_scraper
import pygame
from readwrite import read_file

if __name__ == "__main__":
    a = article_scraper.get_articles(1)
    print(article_scraper.format_article(a[0]))
    
