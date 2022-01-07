print("Importing " + __file__)
import re
from nlps import nlp_matcher
from tokenizers import pos_tokenizer
from finders import noun_phrase_finder
from finders import verb_finder
from converters import pos_to_string_converter
print("Finished importing " + __file__)

def check(text):
    voice_mode={}
    text=re.search(r"\w.*",text).group()
    __passive_result=""
    __active_result=""
    __pos=pos_tokenizer.pos_tokenize(text)
    __verb=[]
    print(__pos)


    if is_interrogative(__pos): #convert interrogative to imperative
            __verb=verb_finder.find_only_verb_question(text,__pos)
            print("The sentence is interrogative.")
            if __pos[-1][0]=="?":
                __pos[-1][0]="."
                __pos[-1][2]="."
            if __pos[-1][1]!="PUNCT":
                __pos.append(['.','PUNCT','.'])
            __pos[__verb[0]][0]=__pos[__verb[0]][3]
            phrase_after_token=[__pos[i] for i in list(range(__verb[0],len(__pos)))]
            __result=pos_to_string_converter.convert(phrase_after_token)
            __passive_result="You are tasked to " +__result


    else:
        __verb=verb_finder.find_only_verb(text,__pos)
        phrase_before_token=[__pos[i] for i in list(range(0,__verb[0]))]
        phrase_before=pos_to_string_converter.convert(phrase_before_token)        
        noun_phrases=noun_phrase_finder.find(phrase_before)
        #convert imperative into passive
        if noun_phrases == [] and __pos[__verb[0]][3]==__pos[__verb[0]][0].lower():
                print("The sentence is imperative.")
                if __pos[-1][0]=="?":
                    __pos[-1][0]="."
                    __pos[-1][2]="."
                if __pos[-1][1]!="PUNCT":
                    __pos.append(['.','PUNCT','.'])
                __pos[__verb[0]][0]=__pos[__verb[0]][3]

                try:
                    phrase_before_token[0][0]=phrase_before_token[0][0].lower()
                    if phrase_before_token[-1][1]=="PUNCT":
                        phrase_before_token.pop()
                except:
                    print("No phrases found before verb")

                phrase_after_token=[__pos[i] for i in list(range(__verb[0],len(__pos)))]
                if phrase_after_token[-1][1]=="PUNCT":
                    for token in phrase_before_token:
                        phrase_after_token.insert(-1, token)
                __passive_result="You are tasked to " + pos_to_string_converter.convert(phrase_after_token) 

        else:
            imp_pattern = [[{"POS":{"NOT_IN":["AUX"]}},{"POS":"AUX","OP":"?"},{"POS":"AUX","OP":"?"}, {"POS":"AUX"},{"TAG":"VBN"},{"LOWER":"to"},{"TAG": "VB"}]]
            matches=nlp_matcher.match(text, imp_pattern)

            if len(matches)>0:
                print("The sentence is in imperative passive form.")
                if __pos[-1][0]=="?":
                    __pos[-1][0]="."
                    __pos[-1][2]="."
                if __pos[-1][1]!="PUNCT":
                    __pos.append(['.','PUNCT','.'])
                __pos[0][0]=__pos[0][0].title()
                __passive_result=pos_to_string_converter.convert(__pos)

            else: #convert declarative into imperative
                print("The sentence is declarative.")
                if __pos[-1][0]=="?":
                    __pos[-1][0]="."
                    __pos[-1][2]="."
                if __pos[-1][1]!="PUNCT":
                    __pos.append(['.','PUNCT','.'])
                __pos[__verb[0]][0]=__pos[__verb[0]][3]
                phrase_after_token=[__pos[i] for i in list(range(__verb[0],len(__pos)))]
                __result=pos_to_string_converter.convert(phrase_after_token)
                __passive_result="You are tasked to " +__result
    
    __active_result= __passive_result[18].upper()+__passive_result[19:]
    voice_mode["active"]=__active_result
    voice_mode["passive"]=__passive_result
    print(voice_mode)
    return voice_mode
    
def is_interrogative(pos):
    #Criteria: 5W1H or AUX pos
    question_words=("who","when","what","where","why","whose","how")
    if pos[0][0] in question_words or pos[0][1] == "AUX":
        return True
    else:
        return False