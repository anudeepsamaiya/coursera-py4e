import re
import urllib.request

from bs4 import BeautifulSoup

url = input("Enter URL : ")
count = int(input("Enter count : "))
pos = int(input("Enter position : "))


for i in range(count):
    print ('Retrieving: %s' %url)    
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    anchor = str(soup('a'))
    links = re.findall('href="(.+?)"', str(anchor))
    url = links[pos-1]
print ('Retrieving: %s' %url)  
print ('Last known by : %s' %re.findall('by_(.+).html', url)[0])
