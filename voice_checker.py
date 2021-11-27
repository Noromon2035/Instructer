import nltk
from nltk.tokenize import word_tokenize

def tokenize(sentence):
    w = word_tokenize(sentence)
    return w

def pos_tag(tokens):
    tagged = nltk.pos_tag(tokens)
    return tagged

def check(sentence):
    tokens = tokenize(sentence)
    tagged = pos_tag(tokens)
    print(tagged)

check("The smell of flowers brings back memories.")