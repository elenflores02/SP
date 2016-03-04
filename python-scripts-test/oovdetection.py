all_words = []
new_words = []
flag = False

for line in open('testforpos.txt'):
	all_words.append(line)

for words in all_words:
	flag = False
	words = words.strip('\n')
	with open('scowl.american.mod.70', 'r') as inF:
	    for line in inF:
	        if words in line:
	        	flag = True
	        	break

	if flag == False:
		new_words.append(words+"	"+"OOV"+"\n")
	else:
		if words != '':
			new_words.append(words+"	"+"IV"+"\n")
		else:
			new_words.append("\t\t\t\n")

f = open('testoov.txt', 'w')
for word in new_words:
	f.write(word)
f.close()