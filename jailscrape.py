
#Adds a tool used to visit websites, makes a csv file
import urllib2, csv
#Adds the BeautifulSoup library, which pulls data from websites
from bs4 import BeautifulSoup

#Opens/creates the jaildata.csv file and indicates we're going to write in it
outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)

#Identifies a website and opens it
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
html = urllib2.urlopen(url).read()

#BeautifulSoup analyzes the jail website
soup = BeautifulSoup(html, "html.parser")

#Tells BeautifulSoup where to find the table we want to scrape
tbody = soup.find('tbody', {'class': 'stripe'})

#Finds the rows in the table
rows = tbody.find_all('tr')

#Finds each cell in the rows it just found
for row in rows:

    cells = row.find_all('td')

#Makes a list
    data = []
#Adds the found cells and their contents into the list
    for cell in cells:
        data.append(cell.text.encode('utf-8'))

#Writes the list (data) into the file we opened
    writer.writerow(data)
