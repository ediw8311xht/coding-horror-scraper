from bs4 import BeautifulSoup
import requests

def get_articles(page):
    articles = []
    url = "https://blog.codinghorror.com/page/%i/" % (page)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for i in soup.find_all("article", class_="post"):
        articles.append(i)
    return articles

def format_article(article):
    start = 0
    tArticle = article.get_text().strip("\n")
    tArticle = tArticle.strip(" ")
    Time = article.find(attrs={"time": "datetime"})
    return tArticle

def get_num_pages():
    url = "https://blog.codinghorror.com/page/2/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    pageNum = soup.find("span", class_="page-number").getText()
    return int(pageNum[10:len(pageNum)])
