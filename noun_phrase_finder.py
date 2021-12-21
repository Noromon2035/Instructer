print("Importing " + __file__)
import spacy
print("Finished importing " + __file__ +"\n")

nlp = spacy.load("en_core_web_sm")

def find(text):
    __nouns=[]
    __doc = nlp(text)
    for np in __doc.noun_chunks:
        __nouns.append(np.text)
    print(__nouns)
    return __nouns
    