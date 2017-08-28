import json
import urllib.request

url = input("Enter Location: ")
print("Retrieving url %s" %url)
data = urllib.request.urlopen(url).read().decode()
data = json.loads(data)

length = len(data)
print("Retrieved %s characters" %length)

items = [item['count'] for item in data['comments']]
print("Count: %s" %len(items))
total = sum(items)
print("Sum: %s" %total)
