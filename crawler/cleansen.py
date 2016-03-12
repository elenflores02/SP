import re

sentences = []
cleansen = []

sen = open('461216.txt', 'r').read()
#separate title, caption, body
sentences = sen.replace("][", "][")
#replace newline with \n
sentences = sentences.replace("\\n", "\n")
#remove unnecessary tags
sentences = sentences.replace("\\u", "")
#remove everything between parentheses ???
sentences = re.sub('\(.*?\)','', sentences)
#parse sentences
sentences = sentences.replace(". ", ".\n")

for index in range(len(sentences)):
	newsen = sentences[index].strip("[")
	newsen = newsen.strip("]")
	cleansen.append(newsen)

f = open('clean461216.txt', 'w')
for word in cleansen:
	f.write(word)
f.close()