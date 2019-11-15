import language_check
import string

tool = language_check.LanguageTool('en-US')

lines = []
f = open("./workbook/dbt_handouts_2nd.txt", "r")
for x in f:
    # print(x)
    matches = tool.check(x)
    # print(len(matches))
    words = x.split(' ')
    if len(matches) == 0 and len(words) >= 5:
        lines.append(x.translate(str.maketrans('', '', string.punctuation)).replace('•• ',''))
f.close()
f = open("./workbook/dbt_handouts_3rd.txt", "w")
f.write(''.join(lines))
f.close()


lines = []
f = open("./workbook/dbt_workbook_2nd.txt", "r")
for x in f:
    # print(x)
    matches = tool.check(x)
    # print(len(matches))
    words = x.split(' ')
    if len(matches) == 0 and len(words) >= 5:
        lines.append(x.translate(str.maketrans('', '', string.punctuation)))
f.close()
f = open("./workbook/dbt_workbook_3rd.txt", "w")
f.write(''.join(lines))
f.close()


