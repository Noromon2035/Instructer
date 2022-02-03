from finders import noun_phrase_finder
from gensim.models import KeyedVectors
from tokenizers import pos_tokenizer
from nltk.corpus import stopwords
from string import punctuation
import wikipedia
import json
import re

sw = stopwords.words('english')
wordvec = KeyedVectors.load("databases/instruct_vector.wordvectors", mmap='r') 
with open("databases/occurences.json", "r") as fp:
    occurences_json=json.load(fp)
occur_quantile=11


def find_occurences(word):
    count=0
    try:
        count=occurences_json[word]
    except:
        count=0
    return count

def simplify(nlp,instruction):
    n_phrases=noun_phrase_finder.find(nlp,instruction)
    print(n_phrases)
    for phrase in n_phrases:
        is_popular=True
        words=pos_tokenizer.pos_tokenize(nlp,phrase)    
        words_nsw=[x for x in words if x[3] not in sw and x[3].istitle()==False and x[3].isalpha()==True]

        unpopular_word=""
        if words_nsw!=None:
            for token in words_nsw:
                word=token[3]
                occurence=find_occurences(word.lower())
                if occurence < occur_quantile:
                    is_popular=False
                    unpopular_word=word
                    break
        if is_popular==False:
            words_sw=[x for x in phrase if x in sw]
            phrase_nsw=phrase
            for word in words_sw:
                phrase_nsw=re.sub(r"\b{}\b".format(word),"",phrase_nsw)
            print(phrase_nsw)

            meaning=""
            try:
                searched_words=wikipedia.search(phrase)
            except:
                return instruction
            print(searched_words)

            phrase_popular=re.sub(r"\b{}\b".format(unpopular_word),"\\\\w+",phrase_nsw)
            phr_pop_match=re.search(r"{}".format(phrase_popular),searched_words[0])
            if phr_pop_match!=None and searched_words[0].lower() != phrase_nsw:
                meaning=searched_words[0]
            else:
                try:
                    meaning=wikipedia.summary(searched_words[0],1)
                    aux_match=re.search(r"is|are|was|were",meaning)
                    if aux_match!=None:
                        span=aux_match.span()
                        meaning=meaning[span[1]+1:-1]
                    else:
                        meaning=""
                except Exception as e:
                    try:
                        phrase_nsw=e.options
                        print(phrase_nsw)
                        meaning=wikipedia.summary(phrase_nsw[0],1)
                        aux_match=re.search(r"is|are|was|were",meaning)
                        if aux_match!=None:
                            span=aux_match.span()
                            meaning=meaning[span[1]+1:-1]
                        else:
                            meaning=""
                    except:
                        return instruction

            meaning=meaning[0].lower()+meaning[1:]
            print("Meaning: " + meaning)
            phrase_format="{} ({})".format(phrase,meaning)
            instruction=re.sub(r"\b{}\b".format(phrase),phrase_format,instruction,1)
    return instruction

if __name__ == "__main__":
    import spacy
    print("Finished exporting")
    nlp = spacy.load("en_core_web_sm")  
    text1="The two parties agreed on a bilateral agreement of using gluteus maximus and gluteus maximus bilateralism for counseling."
    text2="Once it can be safely assumed that the base of the flour-based cake has reached a satisfactory level of cook, firmly grasp handle of your flipping leverage tool with flip-side up and thrust forward using shoulder, engaging glenohumeral joint for smooth motion. Then swallow."  
    result=simplify(nlp,text1)
    print(result)