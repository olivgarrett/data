import csv
import requests, mechanize
from bs4 import BeautifulSoup

csvfile = open('highway.csv', 'a')
jail_writer = csv.writer(csvfile)

#####2.get html
url="https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017"

br = mechanize.Browser()
br.open(url)
html = br.response().read()

#####3.set up soup
soup = BeautifulSoup(html, "html.parser")

