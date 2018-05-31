import glob
import logging
import os

import pandas as pd
from gensim.models.keyedvectors import KeyedVectors

from txtsim import Phrase2VecByMean


FORMAT = '%(asctime)s : %(levelname)s : %(message)s'
logging.basicConfig(format=FORMAT, level=logging.CRITICAL)
logger = logging.getLogger('evaluation')


FILENAME = 'data\\Case1_Dataset.xlsx'

BIN_MODEL_DIR = 'models\\bin'
TXT_MODEL_DIR = 'models\\txt'

TEST_SHEET = 'Test_Set'
MG_DESC_COLUMN = 'Material Group Description'
PS_DESC_COLUMN = 'Procurement Structure Description'
PS_CODE_COLUMN = 'Procurement Structure Code'
PROCUREMENT_STRUCTURE_SHEET = 'Procurement_Structure'
STRUCTURE_DESC_COLUMN = 'Description'
STRUCTURE_CODE_COLUMN = 'Structure Code'

STOP_WORDS = ['/', '=', '+', '*', ',']
TOP_N = 3

IGNOR_FAKE_MODEL = True


def _normalized(str):
    for word in STOP_WORDS:
        str = str.replace(word, ' ')
    return ' '.join(str.lower().split())


def evaluate(test_data_df, prcstructures_df, model):
    correct_count = 0
    for i in range(len(test_data_df)):
        result = model.calculate_similarity(test_data_df[MG_DESC_COLUMN][i], prcstructures_df[STRUCTURE_DESC_COLUMN])
        for n in range(TOP_N):
            if test_data_df[PS_DESC_COLUMN][i] == result[n]['target_doc']:
                correct_count += 1
                break
    return correct_count


def main():
    logger.info("Loading test data")
    test_data_df = pd.read_excel(FILENAME, sheet_name=TEST_SHEET)
    prcstructures_df = pd.read_excel(FILENAME, sheet_name=PROCUREMENT_STRUCTURE_SHEET)

    material_group_count = len(test_data_df)
    prcstructure_count = len(prcstructures_df)
    logger.debug("Totally {} Material Groups and {} Procurement Structures".format(material_group_count, prcstructure_count))

    for i in range(material_group_count):
        test_data_df[MG_DESC_COLUMN][i] = _normalized(test_data_df[MG_DESC_COLUMN][i])
        test_data_df[PS_DESC_COLUMN][i] = _normalized(test_data_df[PS_DESC_COLUMN][i])

    for i in range(prcstructure_count):
        prcstructures_df[STRUCTURE_DESC_COLUMN][i] = _normalized(prcstructures_df[STRUCTURE_DESC_COLUMN][i])
        logger.debug(prcstructures_df[STRUCTURE_DESC_COLUMN][i])

    for model_file in os.listdir(BIN_MODEL_DIR):
        if model_file.startswith('fake_model') and IGNOR_FAKE_MODEL:
            continue
        logger.info("Loading model file {}".format(model_file))
        w2v_model = KeyedVectors.load_word2vec_format(BIN_MODEL_DIR + "\\" + model_file, binary=True)
        model = Phrase2VecByMean(w2v_model)
        correct_count = evaluate(test_data_df, prcstructures_df, model)
        logger.debug("Evaluating {} with Phrase2VecByMean ".format(model_file))
        print("{}\t{}\t{}/{}\t{}".format("Phrase2VecByMean", model_file, correct_count, material_group_count, correct_count * 1.0 / material_group_count))

    for model_file in os.listdir(TXT_MODEL_DIR):
        if model_file.startswith('fake_model') and IGNOR_FAKE_MODEL:
            continue
        logger.info("Loading model file {}".format(model_file))
        w2v_model = KeyedVectors.load_word2vec_format(TXT_MODEL_DIR + "\\" + model_file, binary=False)
        model = Phrase2VecByMean(w2v_model)
        correct_count = evaluate(test_data_df, prcstructures_df, model)
        logger.debug("Evaluating {} with Phrase2VecByMean ".format(model_file))
        print("{}\t{}\t{}/{}\t{}".format("Phrase2VecByMean", model_file, correct_count, material_group_count, correct_count * 1.0 / material_group_count))


if __name__ == '__main__':
    main()
