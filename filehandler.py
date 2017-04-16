import readwrite
from article_scraper import format_date
class FileHandler(object):
    def __init__(self, savefile):
        self.savefile = savefile
        self.get_dates()
    def get_dates(self):
        a = readwrite.read_file(self.savefile)
        self.dates = []
        if a == "no file":
            return False
        else:
            a = a.split("\n")
            for i in a:
                if i[0:2] == "::":
                    self.dates.append(format_date(i[2:].split()))
    def return_dates(self):
        return self.dates

#testing
if __name__ == "__main__":
    a = FileHandler("articles.txt")
    print(a.return_dates())
                
