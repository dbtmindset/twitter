import sys
from textgenrnn import textgenrnn

textgen = textgenrnn()


textgen.train_from_file(sys.argv[1], num_epochs=1)

textgen.save(sys.argv[1]+'.hdf5')