import sys
from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.load(sys.argv[1]+'.hdf5')

textgen.generate()

# list = textgen.generate(n=5, temperature=[0.2], return_as_list=True)
# print(list)

# textgen.generate(interactive=True, top_n=5)

