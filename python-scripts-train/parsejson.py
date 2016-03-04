# FOR GETTING THE INPUT AND OUTPUT

import json

new_data1 = []

with open('jsonlines.txt') as data_file:
	data = json.load(data_file)
	
for i in range(0, 2950):
	for j in range(len(data[i]["input"])):
		new_data1.append(data[i]["input"][j] +"	"+data[i]["output"][j]+"\n")
	new_data1.append("\t\t\t\n")

f = open('trainingio.txt', 'w')
for word in new_data1:
	f.write(word)
f.close()


# FOR GETTING THE TOKENS ONLY

new_data2 = []

with open('jsonlines.txt') as data_file:
	data = json.load(data_file)
	
for i in range(0, 2950):
	for j in range(len(data[i]["input"])):
		new_data2.append(data[i]["input"][j]+"\n")
	new_data2.append("\n")

f = open('trainingforpos.txt', 'w')
for word in new_data2:
	f.write(word)
f.close()