from bs4 import BeautifulSoup
import requests

def getArticles(page):
    articles = []
    url = "https://blog.codinghorror.com/page/%i/" % (page)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for i in soup.find_all("article", class_="post"):
        articles.append(i)
    return articles

def formatArticle(article):
    start = 0
    for i in range(0, len(article)):
        start = i
        if article[i] != " " or article[i] != "\n":
            break
    tArticle = article.get_text()[0:start]
    Time = soup.find(attrs={"time": "datetime"})
    print(Time)
    return tArticle

def getNumPages():
    url = "https://blog.codinghorror.com/page/2/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    pageNum = soup.find("span", class_="page-number").getText()
    return int(pageNum[10:len(pageNum)])
