import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter Location: ")
print("Retrieving url %s" %url)
xml = urllib.request.urlopen(url).read()

length = len(xml)
print("Retrieved %s characters" %length)
elems = ET.fromstring(xml)
count_tags = elems.findall('comments/comment/count')
print("Count: %s" %len(count_tags))
total = sum([int(x.text) for x in count_tags])
print("Sum: %s" %total)
