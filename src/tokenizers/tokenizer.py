print("Importing " + __file__)
from tokenizers import pos_tokenizer
from tokenizers import sentence_tokenizer as st
from tokenizers import subject_predicate_tokenizer as spt
from tokenizers import preposition_tokenizer as prt
from converters import simplifier
print("Finished importing " + __file__)

def convert(text):
    __sentences=[]
    __pos=pos_tokenizer.pos_tokenize(text)
    print(__pos)
    print()
    __sentences=st.convert(text, __pos)
    print("\n\n\n\n\n")
    for sentence in __sentences:
        __sent_pos=pos_tokenizer.pos_tokenize(sentence)
        __simplfied=simplifier.simplify(__sent_pos)
        __simplfied_pos=pos_tokenizer.pos_tokenize(__simplfied)
        print(__simplfied)
        subj_pred=spt.tokenize(__simplfied,__simplfied_pos)
        subj_prep=prt.tokenize(subj_pred["subject"])
        pred_prep=prt.tokenize(subj_pred["predicate"])
        print("\n")

text1="A step-mother below utilises a prosaic language. Not only if they do, but also they acheive beaut by the complexity of their construction, so the way the sentence unfold is amazing."
convert(text1)