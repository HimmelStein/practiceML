import numpy as np
import warnings
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
    results = { 'result':lda_result,
                'logLikelyhood': lda_model.score(dataVector), # the higher the better
                'perplexity': lda_model.perplexity(dataVector), # the lower the better
                'params': lda_model.get_params()
                }
    pprint(results)
    return results


def perform_best_lda_analysis(txtDir='', numOfTxts=None,
                              numTopicsLst=[10,15,20,25,30], learningDecay=[.5,.7,.9]):
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
    model = GridSearchCV(cv=None, error_score='raise',
                         estimator=LatentDirichletAllocation(batch_size=128, doc_topic_prior=None,
                                                             evaluate_every=-1, learning_decay=0.7, learning_method=None,
                                                             learning_offset=10.0, max_doc_update_iter=100, max_iter=10,
                                                             mean_change_tol=0.001, n_components=10, n_jobs=1,
                                                             n_topics=None, perp_tol=0.1, random_state=None,
                                                             topic_word_prior=None, total_samples=1000000.0, verbose=0),
                         fit_params=None, iid=True, n_jobs=1,
                         param_grid={'n_topics': numTopicsLst, 'learning_decay':learningDecay},
                         pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',
                         scoring=None, verbose=0)
    model.fit(dataVector)
    bestLda = model.best_estimator_
    result = {'bestLda': bestLda,
              'params': model.best_params_,
              'logLikelyhood': model.best_score_,
              'perplexity': bestLda.perplexity(dataVector)}
    pprint(result)
    return result


def perform_multi_lda_analysis(txtDir='', numOfTxts=None, numTopicsLst=[10,15,20,25,30], learningDecay=[]):
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
    model = GridSearchCV(cv=None, error_score='raise',
                         estimator=LatentDirichletAllocation(batch_size=128, doc_topic_prior=None,
                                                             evaluate_every=-1, learning_decay=0.7, learning_method=None,
                                                             learning_offset=10.0, max_doc_update_iter=100, max_iter=10,
                                                             mean_change_tol=0.001, n_components=10, n_jobs=1,
                                                             n_topics=None, perp_tol=0.1, random_state=None,
                                                             topic_word_prior=None, total_samples=1000000.0, verbose=0),
                         fit_params=None, iid=True, n_jobs=1,
                         param_grid={'n_topics': numTopicsLst, 'learning_decay':learningDecay},
                         pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',
                         scoring=None, verbose=0)
    model.fit(dataVector)

    logLikelyhoodsDict = dict()
    for decay in learningDecay:
        logLikelyhoodsDict[decay] = [round(gscore.mean_validation_score) for gscore in model.grid_scores_ if
                                        gscore.parameters['learning_decay'] == decay]

    # plot graph
    plt.figure(figsize=(12, 8))
    for k in logLikelyhoodsDict.keys():
        plt.plot(numTopicsLst, logLikelyhoodsDict[k], label=k)
    plt.title("Choosing Optimal LDA Model")
    plt.xlabel("Num Topics")
    plt.ylabel("Log Likelyhood Scores")
    plt.legend(title='Learning decay', loc='best')
    plt.show()


if __name__ == '__main__':
    processTypes = ['single', 'best', 'multi']
    processType = 'multi'
    if processType == 'single':
        perform_lda_analysis(txtDir=cfg.pwc['cleanTxtDir'], numOfTxts=30, numOfTopics=5, maxIter=20,
                             learningMode='online', randomState=100, batchSize=128,
                             evaluateEvery=-1, nJobs=-1)
    if processType == 'best':
        perform_best_lda_analysis(txtDir=cfg.pwc['cleanTxtDir'], numOfTxts=30,
                                  numTopicsLst=[10, 15, 20, 25, 30], learningDecay=[.5, .7, .9])

    if processType == 'multi':
        perform_multi_lda_analysis(txtDir=cfg.pwc['cleanTxtDir'], numOfTxts=30,
                                  numTopicsLst=[10, 15, 20, 25, 30], learningDecay=[.1, .3, .5, .7, .9])

