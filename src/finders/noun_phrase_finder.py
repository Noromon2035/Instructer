try:
    import spacy
except Exception as e:
    print(e)

def find(nlp,text):
    __nouns=[]
    __doc = nlp(text)
    for np in __doc.noun_chunks:
        __nouns.append(np.text)
    return __nouns

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")