#add word length, prefix and suffix

all_words = []
new_words = []
lines = []

for line in open('trainingfeatures.txt'):
	all_words.append(line)

for words in all_words:
	lines = words.split("	")
	lines[2] = lines[2].strip('\n')

	token = str(lines[0])

	prefix = token[:3]
	suffix = token[-3:]

	if lines[0] != '':
		new_words.append(lines[0]+"	"+lines[1]+"	"+lines[2]+"	"+str(len(lines[0]))+"	"+prefix+"	"+suffix+"\n")
	else:
		new_words.append("\t\t\t\n")

f = open('trainingfeatures1.txt', 'w')
for word in new_words:
	f.write(word)
f.close()