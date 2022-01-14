try:
    import spacy
except Exception as e:
    print(e)
    
nlp = spacy.load("en_core_web_sm")

def find(text):
    __nouns=[]
    __doc = nlp(text)
    for np in __doc.noun_chunks:
        __nouns.append(np.text)
    if __nouns !=[]: print(__nouns)
    return __nouns