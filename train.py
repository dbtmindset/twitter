from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('./data/dbt_handouts_pass4.txt', num_epochs=1)

textgen.save('textgenrnn_weights.hdf5')