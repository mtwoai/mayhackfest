import os

from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors


def golve2w2v(src_dir, dst_dir):
    for file in os.listdir("models\\glove"):
        print("Converting {}".format(file))
        glove2word2vec(src_dir + "\\" + file, dest_dir + "\\" + file)


def w2v_txt2bin(src_file, dst_file):
    model = KeyedVectors.load_word2vec_format(src_file, binary=True)
    model.save_word2vec_format(dst_file, binary=False)


def w2v_bin2txt(src_file, dst_file):
    model = KeyedVectors.load_word2vec_format(src_file, binary=False)
    model.save_word2vec_format(dst_file, binary=True)


if __name__ == '__main__':
    # golve2w2v("models\\glove", "models\\txt")
    w2v_bin2txt('models/txt/fake_model.txt', 'models/bin/fake_model.bin')
