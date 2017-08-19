from bs4 import BeautifulSoup as bs
import urllib.request
import re

url = input('Enter - ')
html = urllib.request.urlopen(url)

soup = bs(html, 'html.parser')

comments = soup('span')
s = [int(x) for x in re.findall('[0-9]+', str(comments))]
print('count', len(s))
print('sum', sum(s))

