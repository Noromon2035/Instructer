print("Importing " + __file__)
from os import remove
import re
import spacy
from spacy.matcher import Matcher
#from spacy.tokenizer import Tokenizer
from spacy.tokens import Doc
from nltk.corpus import wordnet as wn

print("Finished importing " + __file__ +"\n")

nlp = spacy.load("en_core_web_sm")
class WhitespaceTokenizer(object):
    def __init__(self, vocab):
        self.vocab = vocab

    def __call__(self, text):
        words = re.split(r'[ .]',text)
        for word in words:
            if word=="":
                words.remove("")
        # All tokens 'own' a subsequent space character in this tokenizer
        spaces = [True] * len(words)
        return Doc(self.vocab, words=words, spaces=spaces)

def tokenize(text):
    __pos=[]
    __doc = nlp(text)
    return __doc

def pos_tokenize(text):
    __pos=[]
    exceptions = nlp.Defaults.tokenizer_exceptions
    nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)
    #nlp.tokenizer = Tokenizer(nlp.vocab, token_match=re.compile(r'[\S+]').match)
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

#pos_tokenize("Are you contacting 98's of the class after eating in cafe along with him?")
