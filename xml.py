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
counts = tree.findall('.//count')

for count in counts:
    