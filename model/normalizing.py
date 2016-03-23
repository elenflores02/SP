all_words = []
new_words = []
lines = []

for line in open('tokenpred.txt'):
	all_words.append(line)

for words in all_words:
	if '	' in words:
		lines = words.split("	")
		if lines[1] == 'OOV':
			with open('lexnorm.txt', 'r') as inF:
			    for line in inF:
			        if lines[0] in line:
			        	new_words.append(lines[0]+"	"+line+"	"+lines[1])
			        	break
			        #else:
			        #normalize
		else:
			new_words.append(lines[0]+"	"+lines[0]+"	"+lines[1])

f = open('normalized.txt', 'w')
for word in new_words:
	f.write(word)
f.close()