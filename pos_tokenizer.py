print("Importing " + __file__)
import spacy
print("Finished importing " + __file__)

nlp = spacy.load("en_core_web_sm")

def tokenize(text):
    __pos=[]
    __doc = nlp(text)
    for token in __doc:
        __pos.append([token.text, token.pos_, token.tag_])
    print("\nThe sentences was tagged.")
    return __pos