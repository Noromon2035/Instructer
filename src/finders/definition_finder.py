print("Importing")
import re
from PyDictionary import PyDictionary
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from string import punctuation

wordvec = KeyedVectors.load("instruct_vector.wordvectors", mmap='r')
dictionary=PyDictionary()
sw = stopwords.words('english')

def find(word,sentence):
    definitions=dictionary.meaning(word,True)
    print(definitions)
    context=re.split("[\s{}]+".format(punctuation),sentence)
    context_nsw=[x for x in context if x not in sw]
    print(context_nsw)

text="repudiate"  
find(text,"Once it can be safely assumed that the base of the flour-based cake has reached a satisfactory level of cook, firmly grasp handle of your flipping leverage tool with flip-side up and thrust forward using shoulder, engaging glenohumeral joint for smooth motion. Then swallow.")
