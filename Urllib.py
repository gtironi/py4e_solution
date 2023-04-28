# To install BeautifulSoup, execute "pip3 install beautifulsoup4" in cmd

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))


links = []
names = []
names_find = []

for i in range(count + 1):
    if i != 0:
        url = links[position - 1]
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    links = []
    names = []
    for tag in tags:
        links.append(tag.get('href', None))
        names.append(tag.contents[0])
    names_find.append(names[position - 1])

