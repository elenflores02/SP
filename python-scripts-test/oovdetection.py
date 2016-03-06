all_words = []
new_words = []
lines = []
flag = False

for line in open('testwithpos.txt'):
	all_words.append(line)

for words in all_words:
	flag = False
	lines = words.split("	")
	with open('scowl.american.mod.70', 'r') as inF:
	    for line in inF:
	        if lines[0] in line:
	        	flag = True
	        	break

	if flag == False:
		if lines[1] == '@':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		elif lines[1] == 'U':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		elif lines[1] == '^':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		elif lines[1] == '#':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		elif lines[1] == '$':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		elif lines[1] == ',':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		else:
			new_words.append(lines[0]+"	"+lines[1]+"	"+"OOV"+"\n")
	else:
		if lines[0] != '':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		else:
			new_words.append("\t\t\t\n")

f = open('testfeatures.txt', 'w')
for word in new_words:
	f.write(word)
f.close()