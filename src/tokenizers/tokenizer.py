print("Importing " + __file__)
import sentence_tokenizer as st
from nlps import nlp_funcs as nlp_funcs
import subject_predicate_tokenizer as spt
import preposition_tokenizer as pt
print("Finished importing " + __file__)

def convert(text):
    __sentences=[]
    __pos=nlp_funcs.pos_tokenize(text)
    __sentences=st.convert(text, __pos)
    print("\n\n\n\n\n")
    for sentence in __sentences:
        __sent_pos=nlp_funcs.pos_tokenize(sentence)
        subj_pred=spt.tokenize(sentence,__sent_pos)
        subj_prep=pt.tokenize(subj_pred["subject"])
        pred_prep=pt.tokenize(subj_pred["predicate"])

convert("As much as possible, the big bad talking wolf's brother is tasked to bring the little pigs in the house then he and she is eating hotdogs of the west, but it failed miserably.")