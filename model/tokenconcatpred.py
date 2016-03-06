all_tokens = []
all_pred = []
new_words = []
lines1 = []
lines2 = []

for line in open('testtokens.txt'):
	if line != "\n":
		all_tokens.append(line)
	else:
		all_tokens.append("\n")

for line in open('predictions.txt'):
	if line != "\n":
		all_pred.append(line)
	else:
		all_pred.append("\n")

for words1, words2 in zip(all_tokens, all_pred):
	lines1 = words1.split("	")
	lines2 = words2.split("	")
	if lines1[0] != "\n" and lines2[0] != "\n":
		lines1[0] = lines1[0].strip('\n')
		lines2[0] = lines2[0].strip('\n')
		new_words.append(lines1[0]+"	"+lines2[0]+"\n")
	else:
		new_words.append("\n")

f = open('tokenpred.txt', 'w')
for word in new_words:
	f.write(word)
f.close()

all_tokens = []
all_pred = []
new_words = []
lines1 = []
lines2 = []

for line in open('testtokens.txt'):
	if line != "\n":
		all_tokens.append(line)
	else:
		all_tokens.append("\n")

for line in open('comparison.txt'):
	if line != "\n":
		all_pred.append(line)
	else:
		all_pred.append("\n")

for words1, words2 in zip(all_tokens, all_pred):
	lines1 = words1.split("	")
	lines2 = words2.split("	")
	if lines1[0] != "\n" and lines2[0] != "\n":
		lines1[0] = lines1[0].strip('\n')
		lines2[1] = lines2[1].strip('\n')
		new_words.append(lines1[0]+"	"+lines2[0]+"	"+lines2[1]+"\n")
	else:
		new_words.append("\n")

f = open('tokeninputpred.txt', 'w')
for word in new_words:
	f.write(word)
f.close()