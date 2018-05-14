import numpy as np
import warnings
import pandas as pd
import os
import re
import spacy
import codecs
from pprint import pprint
import practiceML.config as cfg

from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from pprint import pprint

import pyLDAvis
import pyLDAvis.sklearn
import matplotlib.pyplot as plt


def get_content_words(text, pos = ['NOUN', 'ADJ', 'VERB', 'ADV']):
    nlp = spacy.load('de', disable=['parser', 'ner'])
    doc = nlp(text)
    result = ' '.join([token.lemma_ for token in doc if token.pos_ in pos])
    return result


def perform_lda_analysis(txtDir='', numOfTxts=None, numOfTopics=5, maxIter=20,
                         learningMode='online', randomState=100, batchSize=128,
                         evaluateEvery=-1, nJobs=-1):
    """

    :param txtDir:
    :param numOfTxts: an integer or None for selecting all files
    :param numOfTopics:
    :param maxIter:
    :param learningMode:
    :param randomState:
    :param batchSize:
    :param evaluateEvery:
    :param nJobs:
    :return:
    """
    warnings.simplefilter("ignore", DeprecationWarning)
    txtLst = []
    for fname in os.listdir(txtDir)[:numOfTxts]:
        with codecs.open(os.path.join(cfg.pwc['cleanTxtDir'], fname), 'r', 'utf-8-sig') as fh:
            txt = get_content_words(fh.read())
            txtLst.append(txt)
    txtLst = txtLst
    vectorizer = CountVectorizer(analyzer='word', min_df=4, lowercase=True,
                                 token_pattern='[a-zA-Z0-9]{3,}')

    dataVector = vectorizer.fit_transform(txtLst)
    dataDense = dataVector.todense()
    print("Sparsicity: ", ((dataDense > 0).sum() / dataDense.size) * 100, "%")

    lda_model = LatentDirichletAllocation(n_topics=numOfTopics,
                                          max_iter=maxIter,
                                          learning_method=learningMode,
                                          random_state=randomState,
                                          batch_size=batchSize,
                                          evaluate_every=evaluateEvery,
                                          n_jobs=nJobs)

    lda_result = lda_model.fit_transform(dataVector)
    pprint(lda_result)



if __name__ == '__main__':
    warnings.simplefilter("ignore", DeprecationWarning)
    txtLst = []
    for fname in os.listdir(cfg.pwc['cleanTxtDir'])[:25]:
        with codecs.open(os.path.join(cfg.pwc['cleanTxtDir'], fname), 'r', 'utf-8-sig') as fh:
            txt = get_content_words(fh.read())
            txtLst.append(txt)
    txtLst = txtLst
    vectorizer = CountVectorizer(analyzer='word', min_df=4, lowercase=True,
                                 token_pattern='[a-zA-Z0-9]{3,}')

    dataVector = vectorizer.fit_transform(txtLst)
    dataDense = dataVector.todense()
    print("Sparsicity: ", ((dataDense > 0).sum() / dataDense.size) * 100, "%")

    lda_model = LatentDirichletAllocation(n_topics=5,
                                          max_iter=10,
                                          learning_method='online',
                                          random_state=100,
                                          batch_size=128,
                                          evaluate_every=-1,
                                          n_jobs=-1)

    lda_result = lda_model.fit_transform(dataVector)
    pprint(lda_result)