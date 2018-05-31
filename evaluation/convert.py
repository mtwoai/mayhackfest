import os

from gensim.scripts.glove2word2vec import glove2word2vec

src_dir = "models\\glove"
dest_dir = "models\\txt"

for file in os.listdir("models\\glove"):
    print("Converting {}".format(file))
    glove2word2vec(src_dir + "\\" + file, dest_dir + "\\" + file)
