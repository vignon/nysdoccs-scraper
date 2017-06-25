import argparse
from bs4 import BeautifulSoup
import sys

from CSVreader import CSVread
from WebConnect import webConnect
from dataParser import Parser

data = CSVread(sys.argv[1])

for row in data.get_file():
    print(row)

url = "http://nysdoccslookup.doccs.ny.gov/GCA00P00/WIQ1/WINQ000"
headers = {
    'Content-type': 'application/x-www-form-urlencoded'
    }
data = {
    'K01': 'WINQ000',
    'M00_DIN_FLD1I': '16',
    'M00_DIN_FLD2I': 'A',
    'M00_DIN_FLD3I': '1340'
    }

con = webConnect(url, headers, data)
stuff = con.sendRequest()

parse = Parser(stuff)
stuffs = parse.importResults()
print(stuffs)
