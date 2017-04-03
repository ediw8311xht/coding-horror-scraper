import os.path
import articleScraper
import pygame

def readFile(File):
    String = ""
    with open(File, 'r') as File:
        String = File.read()
    return String

if __name__ == "__main__":
    fn = "articles.txt"
    try:
        a = readFile(fn)
    except IOError:
        File = open(fn, 'w')
        File.write("0\n\n")
        File.close()
        a = readFile(fn)
    numPages = articleScraper.getNumPages()
    less = numPages - int(a[0:10].strip())
    print(less)
