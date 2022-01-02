from nltk.corpus import wordnet as wn

def find_noun_synsets_count(text):
    print("Finding {} noun synsets...".format(text))
    return len(wn.synsets(text, wn.NOUN))

def find_verb_synsets_count(text):
    print("Finding {} verb synsets...".format(text))
    return len(wn.synsets(text, wn.VERB))