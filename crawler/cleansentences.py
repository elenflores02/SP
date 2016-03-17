import re
import os

links = []

for root, dirs, files in os.walk(r'sentences'):
    for file in files:
    	if file.endswith('.txt'):
    		links.append(file)

for index in range(len(links)):
	sentences = []
	cleansen = []
	sen = open('sentences/'+links[index], 'r').read()
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

	for index1 in range(len(sentences)):
		newsen = sentences[index1].strip("[")
		newsen = newsen.strip("]")
		cleansen.append(newsen)

	f = open('clean-business/'+links[index], 'w')
	for word in cleansen:
		f.write(word)
	f.close()