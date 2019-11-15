from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('./workbook/dbt_corpus.txt', num_epochs=1)
for x in range(5):
    # textgen.generate(interactive=True, top_n=5)
    textgen.generate(1, temperature=[0.1])


# textgen.train_from_file('./tweets.txt', num_epochs=10)

# for x in range(5):
#     # textgen.generate(interactive=True, top_n=5)
#     textgen.generate(1, temperature=[0.1])


