#add word length, prefix and suffix, repetitive chars, alphanumeric, normalized form

def hasrepconchar( str ):
	"returns true if str has repetitive consecutive characters"
	if (len(str) == 1):
		return False

	charCount = 1

	for index in range(len(str) - 1):
	    c = str[index];
	    if (c == str[index + 1]):
	        charCount+=1;

	        if (charCount >= 3):
	            return True;
	    else:
	        charCount = 1;

	return False


all_words = []
all_io = []
new_words = []
lines = []


for line in open('trainingfeatures.txt'):
	all_words.append(line)

for line in open('trainingio.txt'):
	all_io.append(line)

for words, words1 in zip(all_words, all_io):
	lines = words.split("	")
	lines1 = words1.split("	")
	lines[2] = lines[2].strip('\n')
	lines1[1] = lines1[1].strip('\n')

	token = str(lines[0])

	prefix = token[:3]
	suffix = token[-3:]

	if lines[0] != '':
		new_words.append(lines[0]+"	"+lines[1]+"	"+str(len(lines[0]))
			+"	"+prefix+"	"+suffix+"	"+str(hasrepconchar(str(lines[0])))
			+"	"+str(str(lines[0]).isalpha())+"	"+lines1[1]+"	"+lines[2]+"\n")
	else:
		new_words.append("\n")


f = open('trainingfeatures.txt', 'w')
for word in new_words:
	f.write(word)
f.close()