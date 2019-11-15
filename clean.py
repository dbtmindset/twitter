import nltk.data
import nltk

nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

lines = []
fp = open("./data/dbt_handouts_pass3.txt")
data = fp.read()
data = ' '.join(data.split())

for x in tokenizer.tokenize(data):
    lines.append(x)

print('\n'.join(lines))
f = open("./data/dbt_handouts_pass4.txt", "w")
f.write('\n'.join(tokenizer.tokenize(data)))
f.close()
