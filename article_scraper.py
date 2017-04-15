from bs4 import BeautifulSoup
from datetime import datetime
import requests

def format_time(Time):
    month_num = {"Jan": 1, "Feb": 2, "Mar": 3,
                 "Apr": 4, "May": 5, "Jun": 6,
                 "Jul": 7, "Aug": 8, "Sep": 9,
                 "Oct": 10, "Nov": 11, "Dec": 12}    
#Gets articles from certain page. Returns list of elemts.
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

if __name__ == "__main__":
    print(
