import nltk.data
import nltk
import language_check
import string
import re

tool = language_check.LanguageTool('en-US')
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

lines = []
fp = open("./data/dbt_handouts_pass1.txt")
data = fp.read()
data = data.replace("\n", ' ').replace('•• ','').replace('*','').replace('Other:', '')
data = re.sub(r'\d+', ' ', data)
data = re.sub(r'[^\x00-\x7f]',r'', data)
data = ' '.join(data.split())

for x in tokenizer.tokenize(data):
    matches = tool.check(x)
    words = x.split(' ')
    if len(matches) == 0 and len(words) >= 8:
        lines.append(x)

print('\n'.join(lines))
f = open("./data/dbt_handouts_pass2.txt", "w")
f.write('\n'.join(tokenizer.tokenize(data)))
f.close()
