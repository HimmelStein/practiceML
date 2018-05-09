import os
import codecs
import json
from pprint import pprint
import practiceML.config as cfg


def cleaning_texts(fdir='', odir='', rmLst=['-\n']):
    assert fdir != odir
    for fn in os.listdir(fdir):
        with codecs.open(os.path.join(fdir, fn), 'r', 'utf-8-sig') as fh:
            txtlst = []
            for ln in fh:
                for rmStr in rmLst:
                    ln = ln.replace(rmStr, '')
                txtlst.append(ln)

            with codecs.open(os.path.join(odir, 'cln_'+fn), 'w', 'utf-8-sig') as oh:
                oh.write(''.join(txtlst))
                oh.flush()


def extract_content_with_key(fdir='', odir='', key='type', value='paragraph'):
    """
    extract context from all json files in the given directory
    :param fdir: input dir
    :param odir: output dir
    :param key:
    :param value:
    :return: None, files with ill-formated lines will be printed.
    """
    assert fdir != odir
    problemLst = []
    for fn in os.listdir(fdir):
        with codecs.open(os.path.join(fdir, fn), 'r', 'utf-8-sig') as fh:
            txtlst = []
            for ln in fh:
                try:
                    data = json.loads(ln)
                    if data.get(key,'') == value:
                        content = data.get('content', '')
                        if type(content) == str:
                            txtlst.append(content)
                except:
                    print('*problem line*: ', ln)
                    if fn not in problemLst:
                        problemLst.append(fn)

            with codecs.open(os.path.join(odir, fn.split('.')[0]+'.txt'), 'w', 'utf-8-sig') as oh:
                if txtlst:
                    oh.write('\n'.join(txtlst))
                    oh.flush()
                else:
                    if fn not in problemLst:
                        problemLst.append(fn)
    print(problemLst)


def list_raw_files(dir):
    """
    list all files in the dir
    :param dir:
    :return: list of files
    """
    dlst = os.listdir(dir)
    pprint(dlst)
    print(len(dlst))
    return dlst


def extracting_texts_from_json():
    extract_content_with_key(fdir=cfg.pwc['rawInputDir'], odir=cfg.pwc['rawTxtDir'])


if __name__ == '__main__':
    problemLst = \
        ['KloecknerCo-QuarterlyReport-2017-Q1.json', 'TAGImmobilien-AnnualReport-2012.json',
         'KloecknerCo-QuarterlyReport-2013-Q3.json', 'SlmSolutionsGroup-QuarterlyReport-2015-Q3.json',
         'Wirecard-QuarterlyReport-2011-Q3.json', 'Telekom-QuarterlyReport-2011-Q3.json',
         'KloecknerCo-QuarterlyReport-2016-Q3.json', 'MLP-AnnualReport-2015.json',
         'Telekom-QuarterlyReport-2011-Q2.json', 'SAF-Holland-QuarterlyReport-2012-Q3.json',
         'Capital_Stage-QuarterlyReport-2013-Q1.json', 'SmaSolarTechnology-AnnualReport-2016.json',
         'Thyssenkrupp-QuarterlyReport-2016-Q3.json', 'MorphoSys-QuarterlyReport-2012-Q3.json',
         'Medigene-QuarterlyReport-2017-Q2.json', 'WCM-QuarterlyReport-2014-Q2.json',
         'Deutsche_Euroshop-QuarterlyReport-2017-Q1.json', 'Thyssenkrupp-QuarterlyReport-2014-Q2.json',
         'Telekom-QuarterlyReport-2012-Q3.json', 'WCM-QuarterlyReport-2013-Q1.json', 'KwsSaat-AnnualReport-2015.json',
         'METRO-AnnualReport-2014.json', 'PATRIZIA-QuarterlyReport-2017-Q1.json',
         'RhoenKlinikum-QuarterlyReport-2011-Q1.json', 'Fresenius-QuarterlyReport-2014-Q3.json',
         'Thyssenkrupp-QuarterlyReport-2014-Q1.json', 'Deutsche_Euroshop-QuarterlyReport-2011-Q1.json',
         'DIC-Asset-QuarterlyReport-2010-Q2.json', 'Telekom-QuarterlyReport-2012-Q1.json',
         'RTLGroup-AnnualReport-2014.json', 'Medigene-QuarterlyReport-2016-Q3.json',
         'Telekom-QuarterlyReport-2012-Q2.json', 'SlmSolutionsGroup-QuarterlyReport-2015-Q2.json',
         'WCM-QuarterlyReport-2016-Q1.json', 'FuchsPetrolub-QuarterlyReport-2012-Q2.json',
         'Thyssenkrupp-QuarterlyReport-2017-Q2.json', 'FuchsPetrolub-QuarterlyReport-2011-Q3.json',
         'Tele_Columbus-QuarterlyReport-2015-Q2.json', 'KloecknerCo-QuarterlyReport-2016-Q2.json',
         'MorphoSys-QuarterlyReport-2017-Q1.json', 'Thyssenkrupp-QuarterlyReport-2014-Q3.json',
         'Beiersdorf-QuarterlyReport-2016-Q1.json', 'Steinhoff-QuarterlyReport-2011-Q2.json',
         'METRO-QuarterlyReport-2013-Q2.json', 'Medigene-QuarterlyReport-2017-Q1.json',
         'MorphoSys-QuarterlyReport-2016-Q1.json']

    cleaning_texts(fdir=cfg.pwc['rawTxtDir'], odir=cfg.pwc['cleanTxtDir'])

