from bs4 import BeautifulSoup

content = open("461216.html",'r').read()
soup = BeautifulSoup(content, 'html.parser')
result = soup.findAll('div',{'class':'field-item even'})

f = open('461216.txt', 'w')
f.write(str(result))
f.close()

content2 = open("461216.txt",'r').read()
soup2 = BeautifulSoup(content2, 'html.parser')
result2 = soup2.get_text()

f = open('461216.txt', 'w')
f.write(str(result2))
f.close()