import spacy
from spacy import tokens

nlp = spacy.load("en_core_web_sm")

def convert(text):
    __pos_tokens=[]
    __doc = nlp(text)
    for token in __doc:
        __pos_tokens.append([token.text, token.pos_, token.tag_])
        print(__pos_tokens[-1])
    print("The instruction was tokenized.")
    return __pos_tokens