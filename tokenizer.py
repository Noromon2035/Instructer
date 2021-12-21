print("Importing " + __file__)
import sentence_tokenizer
import nlp_funcs
import subject_predicate_tokenizer
import preposition_tokenizer
print("Finished importing " + __file__)

def convert(text):
    __sentences=[]
    __pos=nlp_funcs.pos_tokenize(text)
    __sentences=sentence_tokenizer.convert(text, __pos)
    print("\n\n\n\n\n")
    for sentence in __sentences:
        __sent_pos=nlp_funcs.pos_tokenize(sentence)
        subj_pred=subject_predicate_tokenizer.tokenize(sentence,__sent_pos)
        subj_prep=preposition_tokenizer.tokenize(subj_pred["subject"])
        pred_prep=preposition_tokenizer.tokenize(subj_pred["predicate"])

convert("As much as possible, the big bad talking wolf's brother is tasked to bring the little pigs in the house then he and she is eating hotdogs of the west, but it failed miserably.")