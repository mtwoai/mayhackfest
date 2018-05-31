import logging

from gensim.models.keyedvectors import KeyedVectors


logger = logging.getLogger('txtsim')


class BaseTxtSim(object):
    """Docstring for class TxtSim"""

    def __init__(self, w2v_model, threshold=0):
        super(BaseTxtSim, self).__init__()
        self.w2v_model = w2v_model
        self._nonexist_docs = set()
        self.threshold = threshold


    def _calculate_score(self, src_words, target_words):
        return 0.0


    def calculate_similarity(self, source_doc, target_docs=[]):
        if isinstance(target_docs, str):
            target_docs = [target_docs]

        results = []
        for target_doc in target_docs:
            src_words = self._filter_nonexist(source_doc.split())
            target_words = self._filter_nonexist(target_doc.split())

            sim_score = self._calculate_score(src_words, target_words)
            if sim_score >= self.threshold:
                results.append({
                    'score': sim_score,
                    'target_doc': target_doc
                })
            else:
                results.append({
                    'score': sim_score,
                    'target_doc': 'general'
                })

        ''' Sort results by score in desc order '''
        results.sort(key=lambda k: k['score'], reverse=True)

        if len(results) > 0:
            logger.debug("result for [{0}]: {1}".format(source_doc, results[0]))

        return results


    def _filter_nonexist(self, words):
        result = []
        for word in words:
            try:
                self.w2v_model[word]
                result.append(word)
            except KeyError:
                pass

        if len(result) == 0 and ' '.join(words) not in self._nonexist_docs:
            self._nonexist_docs.add(' '.join(words))
            logger.debug('[{0}] is invalid'.format(' '.join(words)))
        return result


class Phrase2VecByMean(BaseTxtSim):

    def __init__(self, *args, **kwargs):
        super(Phrase2VecByMean, self).__init__(*args, **kwargs)
        pass

    def _calculate_score(self, src_words, target_words):
        if len(src_words) > 0 and len(target_words) > 0:
            return self.w2v_model.n_similarity(
                src_words, target_words)
        return 0.0

