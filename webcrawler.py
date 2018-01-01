
import requests
from bs4 import BeautifulSoup

# def spider(maxpages):
# 	page = 1
# 	while page < maxpages:
url =''
sourcecode = requests.get(url)

plaintext = sourcecode.text
soup = BeautifulSoup(plaintext)
i = 0
for link in soup.findAll('a',{'class':'#enter classname here'}):
	href = url + link.get('href')
	title = link.string
	i = i+1 
	row = str(i) + ',' + title + ',' + href + '\n'
	for p in link:
		f = open("data.csv", "a")
		columnTitleRow = "no, name ,link \n"
		f.write(row)   
		f.close()
    


