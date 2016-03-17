from bs4 import BeautifulSoup
import os

links = []

for root, dirs, files in os.walk(r'html-files'):
    for file in files:
    	if file.endswith('.html'):
    		links.append(file)

for index in range(len(links)):
	content = open("html-files/"+links[index],'r').read()
	soup = BeautifulSoup(content, 'html.parser')
	title = soup.findAll('h1',{'class':'title'})
	caption = soup.findAll('div',{'class':'image-caption clearfix'})
	result = soup.findAll('div',{'class':'field-item even'})

	f = open('sentences/'+links[index]+'.txt', 'w')
	f.write(str(title))
	f.write(str(caption))
	f.write(str(result))
	f.close()

	content2 = open("sentences/"+links[index]+".txt",'r').read()
	soup2 = BeautifulSoup(content2, 'html.parser')
	result2 = soup2.get_text()


	f = open('sentences/'+links[index]+'.txt', 'w')
	f.write(str(result2))
	f.close()