from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time

def get_seconds(Date):
    return time.mktime(Date.timetuple())

def format_date(Date):
    month_num = {"jan": 1, "feb": 2, "mar": 3,
                 "apr": 4, "may": 5, "jun": 6,
                 "jul": 7, "aug": 8, "sep": 9,
                 "oct": 10, "nov": 11, "dec": 12}
    date_num = [0, 0, 0]
    for i in Date:
        if str(i).lower() not in month_num:
            if int(i) > 31:
                date_num[0] = int(i)
            else:
                date_num[2] = int(i)
        else:
            date_num[1] = month_num[i.lower()]
    return datetime(date_num[0], date_num[1], date_num[2])
        
#Gets articles from certain page. Returns list of elements.
def get_articles(page):
    articles = []
    url = "https://blog.codinghorror.com/page/%i/" % (page)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for i in soup.find_all("article", class_="post"):
        articles.append(i)
    return articles

#This returns time of article then text
def format_article(article):
    start = 0
    tArticle = article.get_text().strip("\n")
    tArticle = tArticle.strip(" ")
    time_article = tArticle.split("\n", 1)
    return time_article

def get_num_pages():
    url = "https://blog.codinghorror.com/page/2/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    pageNum = soup.find("span", class_="page-number").getText()
    return int(pageNum[10:len(pageNum)])
