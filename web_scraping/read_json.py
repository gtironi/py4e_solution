import json
import urllib.request, urllib.parse, urllib.error

url = ' http://py4e-data.dr-chuck.net/comments_1762292.json'
uh = urllib.request.urlopen(url)

data = uh.read()
info = json.loads(data)

sum = 0
for item in info['comments']:
    sum += item['count']

print(sum)

