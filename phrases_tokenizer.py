print("Importing " + __file__)
from numpy import conj
import spacy
import conjuct_tokenizer
import re
print("Finished importing " + __file__ +"\n")

nlp = spacy.load("en_core_web_sm")

def check(text):
    __tokens={}
    __nouns=[]
    __pos=[]

    __doc = nlp(text)

    for token in __doc:
        __pos.append([token.text, token.pos_, token.tag_])
    __tokens["pos"]=__pos
    print(__tokens["pos"])
    print("The instruction was tagged.\n")

    for np in __doc.noun_chunks:
        __nouns.append(np.text)
    __tokens["noun_phrases"]=__nouns
    print(__tokens["noun_phrases"])
    print("Noun phrases were detected.\n")

    __tokens["conjunctions"]=conjuct_tokenizer.tokenize(text)
    print(__tokens["conjunctions"])
    print("Conjuctions were detected.\n")
    return __tokens

check("The big bad talking wolf is tasked to bring the little dogs and pigs, while he is eating")

