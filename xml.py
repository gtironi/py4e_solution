import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
data = urlopen(url, context=ctx).read()

print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
comments = tree.findall('.//comment')
print("Count", len(comments))
sum = 0

for comment in comments:
    sum = sum + int(comment.find('count').text)

print (sum)