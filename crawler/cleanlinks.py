all_links = []
new_words = []
lines = []

for line in open('items.csv'):
	all_links.append(line)

for words in all_links:
	lines = words.split(",/")
	if "title" not in lines[0]:
		link = lines[1][:-3]
		new_words.append("http://www.sunstar.com.ph/" + link + "\n")

f = open('links.txt', 'w')
for word in new_words:
	f.write(word)
f.close()