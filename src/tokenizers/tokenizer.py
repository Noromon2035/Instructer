print("Importing " + __file__)
from tokenizers import pos_tokenizer
from tokenizers import sentence_tokenizer as st
from tokenizers import subject_predicate_tokenizer as spt
from tokenizers import preposition_tokenizer as prt
from converters import simplifier
from checkers import voice_checker
print("Finished importing " + __file__)

def convert(text,receiver ):
    __sentences=[]
    __answered_questions=set()
    __pos=pos_tokenizer.pos_tokenize(text)
    print(__pos)
    print()
    __sentences=st.convert(text, __pos)
    print("\n\n\n\n\n")
    for sentence_token in __sentences:
        sentence=sentence_token[1]
        __sent_pos=pos_tokenizer.pos_tokenize(sentence)
        __simplfied=simplifier.simplify(__sent_pos)
        __simplfied_pos=pos_tokenizer.pos_tokenize(__simplfied)
        print(__simplfied)
        subj_pred=spt.tokenize(__simplfied,__simplfied_pos)
        subj_prep=prt.tokenize(subj_pred["subject"])
        if subj_prep != None:
            for prep in subj_prep:
                __answered_questions.add(prep[2])
        pred_prep=prt.tokenize(subj_pred["predicate"])
        if pred_prep !=None:
            for prep in pred_prep:
                __answered_questions.add(prep[2])
        __imperatived=voice_checker.check(__simplfied)
        print(__imperatived["active"])
        print("\n")
    print(__answered_questions)

text1="A step-mother below utilises a prosaic language by speaking. Not only if they do, but also they acheive beaut by the complexity of their construction, so the way the sentence unfold is amazing."
convert(text1,"Jomar")