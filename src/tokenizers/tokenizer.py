print("Importing " + __file__)
from tokenizers import sentence_tokenizer as st
from nlps import nlp_funcs as nlp_funcs
from tokenizers import subject_predicate_tokenizer as spt
from tokenizers import preposition_tokenizer as pt
print("Finished importing " + __file__)

def convert(text):
    __sentences=[]
    __pos=nlp_funcs.pos_tokenize(text)
    __sentences=st.convert(text, __pos)
    print("\n\n\n\n\n")
    for sentence in __sentences:
        __sent_pos=nlp_funcs.pos_tokenize(sentence)
        print(__sent_pos)
        subj_pred=spt.tokenize(sentence,__sent_pos)
        subj_prep=pt.tokenize(subj_pred["subject"])
        pred_prep=pt.tokenize(subj_pred["predicate"])

convert("You are tasked to swim under the sea while eating breakfast")