from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('./data/dbt_handouts_pass3.txt', num_epochs=1)
textgen.generate()


# for x in range(5):
    # textgen.generate(interactive=True, top_n=5)
    # textgen.generate(1, temperature=[0.1])


# textgen.train_from_file('./tweets.txt', num_epochs=10)

# for x in range(5):
#     # textgen.generate(interactive=True, top_n=5)
#     textgen.generate(1, temperature=[0.1])


