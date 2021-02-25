#!/usr/bin/env python3
# Print Tool Catalogue

from re import DOTALL, search
from xml.dom.minidom import parseString
from sys import exit

with open('src/catalogue.html', 'rt') as stream:
  markup = stream.read()

markup = search(r'<tbody>.*</tbody>', markup, flags=DOTALL)

try:
  etree = parseString(markup.group())
except:
  sys.exit(1)

tools = etree.getElementsByTagName('td')

for index in range(0, tools.length, 2):
  print('\033[36m', tools[index].firstChild.firstChild.data.ljust(16), end='\033[0m  ')
  print(tools[index + 1].firstChild.data)
