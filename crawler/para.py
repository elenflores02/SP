from bs4 import BeautifulSoup

content = open("461216.html",'r').read()
soup = BeautifulSoup(content, 'html.parser')
title = soup.findAll('h1',{'class':'title'})
caption = soup.findAll('div',{'class':'image-caption clearfix'})
result = soup.findAll('div',{'class':'field-item even'})

f = open('461216.txt', 'w')
f.write(str(title))
f.write(str(caption))
f.write(str(result))
f.close()

content2 = open("461216.txt",'r').read()
soup2 = BeautifulSoup(content2, 'html.parser')
result2 = soup2.get_text()


f = open('461216.txt', 'w')
f.write(str(result2))
f.close()