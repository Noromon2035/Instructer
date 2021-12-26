print("Importing " + __file__)
import spacy
from spacy.matcher import Matcher
from nltk.corpus import wordnet as wn
print("Finished importing " + __file__ +"\n")

nlp = spacy.load("en_core_web_sm")

def pos_tokenize(text):
    __pos=[]
    __doc = nlp(text)
    for token in __doc:
        __pos.append([token.text, token.pos_, token.tag_,token.lemma_])
    return __pos

def find_noun_phrases(text):
    __nouns=[]
    __doc = nlp(text)
    for np in __doc.noun_chunks:
        __nouns.append(np.text)
    if __nouns !=[]: print(__nouns)
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
    print("Finding {} noun synsets...".format(text))
    return len(wn.synsets(text, wn.NOUN))

def find_verb_synsets_count(text):
    print("Finding {} verb synsets...".format(text))
    return len(wn.synsets(text, wn.VERB))

def match(text, pattern):
    matcher = Matcher(nlp.vocab)
    #pattern [{:},{:}]
    matcher.add("matcher", pattern)
    doc = nlp(text)
    matches = matcher(doc, as_spans=True)
    for span in matches:
        print(span.text)
    return matches

find_noun_phrases("Are you contacting 98's of the class after eating in cafe along with him?")
