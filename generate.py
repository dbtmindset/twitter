from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.load('textgenrnn_weights.hdf5')

list = textgen.generate(n=10, temperature=[0.1], return_as_list=True)
# textgen.generate(interactive=True, top_n=5)

# for x in range(5):
    # textgen.generate(interactive=True, top_n=5)
    # textgen.generate(1, temperature=[0.1])


# textgen.train_from_file('./tweets.txt', num_epochs=10)

# for x in range(5):
#     # textgen.generate(interactive=True, top_n=5)
#     textgen.generate(1, temperature=[0.1])


print(list)