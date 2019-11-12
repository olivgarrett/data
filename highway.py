import csv
import requests, mechanize
from bs4 import BeautifulSoup

csvfile = open('highway.csv', 'a')
highway = csv.writer(csvfile)

#####2.get html
url="https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017"
html = requests.get(url).content

#####3.set up soup
soup = BeautifulSoup(html, "html.parser")

table = soup.find('table', {'class': 'accidentOutput'})
rows = table.find_all('tr')

for row in rows:

	tds = row.find_all('td')

	output = []
	for td in tds:
		output.append(td.text.strip())

	highway.writerow(output)
