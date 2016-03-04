all_pos = []
all_io = []
all_oov = []
new_words = []
lines1 = []
lines2 = []

for line in open('testwithpos.txt'):
	if line != "\t\t\t\n":
		all_pos.append(line)
	else:
		all_pos.append("\n")

for line in open('testoov.txt'):
	if line != "\t\t\t\n":
		all_oov.append(line)
	else:
		all_oov.append("\n")

for words1, words3 in zip(all_pos, all_oov):
	lines1 = words1.split("	")
	lines3 = words3.split("	")
	if lines1[0] != "\n" and lines3[0] != "\n":
		lines3[1] = lines3[1].strip('\n')
		new_words.append(lines1[0]+"	"+lines1[1]+"	"+lines3[1]+"\n")
	else:
		new_words.append("\n")

f = open('testfeatures.txt', 'w')
for word in new_words:
	f.write(word)
f.close()