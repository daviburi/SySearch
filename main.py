from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup
import re
import codecs

#Getting page source
def getPageSource(url):
    page = urlopen(url)
    html = page.read()
    return BeautifulSoup(html)

if __name__ == "__main__":
    url = "http://www.sports.ru/tags/1046171.html?type=news"
    soup = getPageSource(url).prettify()

    print(soup.encode('utf-8'))