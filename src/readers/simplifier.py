import time
start=time.time()

import pyinflect
import statistics
import math
from gensim.models import KeyedVectors
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nlps import nlp_funcs
from converters import pos_to_string_converter

sw = stopwords.words('english')
wordnet_pos=("NOUN","VERB","ADV","ADJ")
wordvec = KeyedVectors.load("instruct_vector.wordvectors", mmap='r')

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def spacy_pos_to_wordnet(tag):
    if tag=="NOUN":
        return wn.NOUN
    elif tag=="VERB":
        return wn.VERB
    elif tag=="ADJ":
        return wn.ADJ
    elif tag=="ADV":
        return wn.ADV

def best_synonym_1(orig_token,above_median,pos): 
    context_tokens=[]
    dist=2
    left_side=orig_token[4]-dist
    right_side=orig_token[4]+dist+1
    for i in list(range(left_side,right_side)):
        try:
            if i != orig_token[4]:
                context_tokens.append(pos[i])
        except:
            continue

    orig_token_errors=[]
    for context in context_tokens:
        try:
            orig_token_errors.append(wordvec.similarity(orig_token[3],context[3]))
        except:
            orig_token_errors.append(0)

    total_errors=[]
    for token in above_median:
        total_error=[]
        total_error.append(token[0])
        error=0
        for i in list(range(0,len(orig_token_errors))):
            try:
                similarity=wordvec.similarity(token[0],context_tokens[i][3])
                error+=abs(similarity-orig_token_errors[i])
                print("{} and {}: {} out of {}".format(token[0],context_tokens[i][3],error,orig_token_errors[i]))
            except:
                error+=0
        total_error.append(error)
        total_errors.append(total_error)
    print(total_errors)

def best_synonym_2(orig_token,tokens,pos):
    if len(tokens)<=0:
        return [orig_token[3],1]
    data_set=[token[1] for token in tokens]
    median=statistics.median_high(data_set)
    for token in tokens:
        if token[0]==orig_token[3]:
            if token[1]<median:
                above_median=[token for token in tokens if token[1]>median]
                return best_synonym_1(orig_token,above_median,pos)
            else:
                return token


def simplify(text,pos):
    pos_without_sw = [token for token in pos if token[0].lower() not in sw and token[1] in wordnet_pos]
    indexes_without_sw = [i for i in list(range(0,len(pos))) if pos[i][0].lower() not in sw and pos[i][1] in wordnet_pos]
    doc=read_text_file("model-vocab-1.txt")

    for i in list(range(0,len(pos_without_sw))):
        pos_without_sw[i].append(i)
    del indexes_without_sw
    print(pos_without_sw)

    final_tokens=[]
    for token in pos_without_sw:
        tag=spacy_pos_to_wordnet(token[1])
        synonyms=wn.synsets(token[3].lower(), pos=tag)

        #get all synonyms of each token as raw_string
        raw_synonyms=set()
        for syn in synonyms:
            raw_synonyms.add(token[3])
            raw_syns=syn.lemmas()
            for raw_syn in raw_syns:
                raw=str(raw_syn.name())
                raw_synonyms.add(raw.replace("_"," "))            
        
        #find occurences of each tokens
        synonym_tokens=[]
        for syn in raw_synonyms:
            occurences=doc.count("{} ".format(syn))
            if occurences!=0:
                synonym_tokens.append([syn,occurences])
        print(synonym_tokens)
        
        #choose the best synonym
        final_token=best_synonym_2(token,synonym_tokens,pos_without_sw)
        final_tokens.append(final_token)
        print("Best synonym: {}\n".format(final_token[0]))

    print()
    print(final_tokens)
    doc_tokens=nlp_funcs.tokenize(text)
    for i in list(range(0,len(final_tokens))):
        if final_tokens[i]==None:
            continue
        pos[indexes_without_sw[i]][3]=final_tokens[i][0]
        doc_tokens[i].lemma_=final_tokens[i][0]
        try:
            pos[indexes_without_sw[i]][0]=doc_tokens[i]._.inflect(pos[indexes_without_sw[i]][2]).lower()
        except:
            continue
    return pos_to_string_converter.convert(pos)


text1="Few sentences below use prosaic language, but if they do, they acheive beauty by the complexity of their construction, the way the sentence unspools."
text2="I find beautiful language necessary but not sufficient."
text3="But if a sentence is only beautiful, and doesn't stretch for anything more, I feel admiration but not love. After all, there are millions of gorgeous lines of prose, and we only have so much attention."
sample=nlp_funcs.pos_tokenize(text1)
result=simplify(text1,sample)
print(result)

end=time.time()
print("Runtime={}".format(end-start))