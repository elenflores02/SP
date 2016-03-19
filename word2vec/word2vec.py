import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#my_model = gensim.models.Word2Vec.load('mymodel.txt')

all_words = []
lines = []
sentences = []

for line in open('sen.txt'):
	lines = line.split(" ")
	new_words = []
	for x in lines:
		x = x.strip('\n')
		if x != '':
			new_words.append(x)
	if new_words:
		sentences.append(new_words)

model = gensim.models.Word2Vec(sentences, min_count=10, size=100, window=10)

model.save('mymodel.txt')

'''
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
[('queen', 0.50882536)]
model.doesnt_match("breakfast cereal dinner lunch".split())
'cereal'
model.similarity('woman', 'man')
0.73723527

model['computer']  # raw NumPy vector of a word
array([-0.00449447, -0.00310097,  0.02421786, ...], dtype=float32)
'''
