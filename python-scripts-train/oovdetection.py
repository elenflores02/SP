all_words = []
new_words = []
lines = []
flag = False

for line in open('trainingwithpos.txt'):
	all_words.append(line)

for words in all_words:
	flag = False
	lines = words.split("	")
	with open('scowl.american.mod.70', 'r') as inF:
	    for line in inF:
	        if lines[0] in line:
	        	flag = True
	        	break

	# token is not in dictionary
	if flag == False:
		#mentions
		if lines[1] == '@':	
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		#urls
		elif lines[1] == 'U':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		#pronouns
		elif lines[1] == '^':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		#hashtags
		elif lines[1] == '#':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		#numerals
		elif lines[1] == '$':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		#punctuations
		elif lines[1] == ',':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		else:
			new_words.append(lines[0]+"	"+lines[1]+"	"+"OOV"+"\n")
	else:
		if lines[0] != '':
			new_words.append(lines[0]+"	"+lines[1]+"	"+"IV"+"\n")
		else:
			new_words.append("\t\t\t\n")

f = open('trainingfeatures.txt', 'w')
for word in new_words:
	f.write(word)
f.close()