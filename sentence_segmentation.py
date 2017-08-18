import urllib
import re
import bs4 as bs
url="https://www.analyticsvidhya.com/blog/2015/06/machine-learning-basics/"
handle=urllib.request.urlopen(url)
ht=handle.read()
soup=bs.BeautifulSoup(ht,'html.parser') 
#lxml is a parser
#print(soup.title) prints the title
#print(soup.title.string) prints without tags
#print(soup.find_all('p')) prints all those with paragraph tags
a=""
for paragraph in soup.find_all('p'):
    a=a+str(paragraph.text)
#print(a)
#b=a.split('. ')
for text in a.split('.'):
    print(text)