import spacy
import os
import codecs
from spacy.lang.de import German
import re
import collections
import practiceML.config as cfg


def create_p3ml_vocab(fdir='', odir=''):
    nlp = spacy.load('de_core_news_sm')
    deTokenizer = German().Defaults.create_tokenizer(nlp)
    i = 0
    for fn in os.listdir(fdir):
        print(i, fn)
        i += 1
        with codecs.open(os.path.join(fdir, fn), 'r', 'utf-8-sig') as fh:
            txt = fh.read()
            # txtLst = list(set(re.sub(r'[^\w\s]',' ', txt).split()))
            txtLst = [str(s) for s in list(deTokenizer(txt))]
            counter = collections.Counter(txtLst)
        ofile = 'VOC_'+fn
        codecs.open(os.path.join(odir, ofile), 'w').close()
        with codecs.open(os.path.join(odir, ofile), 'a+') as ofh:
            keys = list(counter.keys())
            keys.sort()
            for key in keys:
                if isinstance(key, str):
                    ofh.write(' '.join([key, str(counter[key])])+'\n')


if __name__ == '__main__':
    create_p3ml_vocab(fdir=cfg.pwc['cleanTxtDir'], odir=cfg.pwc['KDDir'])

