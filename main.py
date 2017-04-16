import os.path
import article_scraper
from readwrite import read_file

if __name__ == "__main__":
    a = article_scraper.get_articles(1)
    a = article_scraper.format_article(a[0])
    TT = article_scraper.format_date(a[0].split())
    print(test(TT))
    
