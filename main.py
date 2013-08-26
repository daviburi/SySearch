#import bs4
from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "http://www.sports.ru/tags/1046171.html?type=news"
source = urlopen(url)

content = source.read() 
source.close()

print content
from urllib2 import urlopen

url = "http://www.sports.ru/tags/1046171.html?type=news"
source = urlopen(url)

content = source.read() 
source.close()

print content