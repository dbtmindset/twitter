import nltk.data
import nltk

nltk.download('punkt')

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

fp = open("./workbook/dbt_workbook.txt")
data = fp.read()
# print('\n'.join(tokenizer.tokenize(data)))
f = open("./workbook/dbt_workbook_2nd.txt", "a")
f.write('\n'.join(tokenizer.tokenize(data)))
f.close()

fp = open("./workbook/dbt_handouts.txt")
data = fp.read()
# print('\n'.join(tokenizer.tokenize(data)))
f = open("./workbook/dbt_handouts_2nd.txt", "a")
f.write('\n'.join(tokenizer.tokenize(data)))
f.close()