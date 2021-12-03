print("Importing " + __file__)
import spacy
from spacy import tokens
print("Finished importing " + __file__)

nlp = spacy.load("en_core_web_sm")

def convert(text):

    __nouns=[]
    __pos_tokens=[]
    __tokens = {}

    __doc = nlp(text)
    for token in __doc:
        __pos_tokens.append([token.text, token.pos_, token.tag_])
        print(__pos_tokens[-1])
    __tokens["pos"]=__pos_tokens
    print("The instruction was tokenized.")

    for np in __doc.noun_chunks:
        __nouns.append(np.text)
        print(np.text)
    __tokens["nouns"]=__nouns

    print("Noun phrases were detected.")
    return __tokens