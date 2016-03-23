# FOR GETTING THE TWEETS

import json

new_data = []

tweets = []

for line in open('training.txt', 'r'):
    tweets.append(json.loads(line))
	
for i in range(len(tweets)):
	new_data.append(tweets[i]["text"].encode('utf-8').strip() + "\n")
	#new_data.append("\t\t\t\n")

f = open('tweets.txt', 'w')
for word in new_data:
	f.write(word)
f.close()