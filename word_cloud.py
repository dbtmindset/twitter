import string
import json

min_rank = 50
exclude_list = ['of', 'and', 'Your', 'your', 'be', 'in', 'as', 'with', 'the',
    'to', 'are', 'that', 'when', 'make', 'can', 'at', 'it', 'an', 'is', 'all,', 'if',
    'pp', 'do', 'how', 'p', 'them', 'no', 'this' ,'worksheets', 'I','for', 'by',
    'yourself', 'down', 'my', 'who', 'one', 'what', 'not', 'Handout', 'have', 'If',
    'When', 'get', 'each', 'dont', 'go', 'into', 'Do']


f = open("./data/dbt_handouts_pass4.txt", "r")
data = f.read().replace('\n', ' ')
data = data.translate(str.maketrans('', '', string.punctuation))
words = data.split(' ')

counts = dict()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

newDict = dict(filter(lambda elem: elem[1] > min_rank and not any(elem[0] in s for s in exclude_list), counts.items()))
ranked = sorted(newDict.items(), key = lambda kv:(kv[1], kv[0]))
ranked.reverse()

# print(ranked)   

# print(json.dumps(ranked))

output = []
for r in ranked: 
    obj = {}
    # print(r[0], r[1], end=' ')
    obj['name'] = r[0]
    obj['value'] = r[1]
    output.append(obj)

print(json.dumps(output))