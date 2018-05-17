from practiceML.pre.extract_texts import list_raw_files, extracting_texts_from_json, cleaning_texts, process_all_files, without_hyphens
from practiceML.pre.statistics import create_p3ml_vocab
from practiceML.core.lda import create_lda_model
import practiceML.config as cfg
from pprint import pprint
#import json

def show_state_of_directories():
    for key in cfg.pwc.keys():
        directory = cfg.pwc[key]
        print('\n --- ', key, ': ', directory, ' ---')
        list_raw_files(directory)


if __name__ == '__main__':
    
    show_state_of_directories()
    
    extracting_texts_from_json()
    cleaning_texts(fdir=cfg.pwc['rawTxtDir'], odir=cfg.pwc['cleanTxtDir'])
    process_all_files(cfg.pwc['rawTxtDir'], cfg.pwc['cleanTxtDir'], 'cln3_', '.txt', without_hyphens)

    create_p3ml_vocab(fdir=cfg.pwc['cleanTxtDir'], odir=cfg.pwc['KDDir'])


#    create_p3ml_vocab(fdir=cfg.pwc['cleanTxtDir'], odir=cfg.pwc['KDDir'])
#    lda_model = create_lda_model()
#    pprint(lda_model)
    
    show_state_of_directories()

