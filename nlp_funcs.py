print("Importing " + __file__)
import spacy
from nltk.corpus import wordnet as wn
print("Finished importing " + __file__ +"\n")

nlp = spacy.load("en_core_web_sm")

def pos_tokenize(text):
    __pos=[]
    __doc = nlp(text)
    for token in __doc:
        __pos.append([token.text, token.pos_, token.tag_])
    print("\nThe text was tagged.")
    return __pos

def find_noun_phrases(text):
    __nouns=[]
    __doc = nlp(text)
    for np in __doc.noun_chunks:
        __nouns.append(np.text)
    if __nouns !=[]: print("\nNouns were found.")
    return __nouns

def lemmatize(text):
    __lemmas=[]
    lemmatizer = nlp.get_pipe("lemmatizer")
    __doc = nlp(text)
    for token in __doc:
        __lemmas.append(token.lemma_)
    print("\nThe text was lemmatized")
    return __lemmas

def find_noun_synsets_count(text):
    return len(wn.synsets(text, wn.NOUN))

def find_verb_synsets_count(text):
    return len(wn.synsets(text, wn.VERB))
