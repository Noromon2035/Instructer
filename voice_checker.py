print("Importing " + __file__)
import nlp_funcs
import verb_finder
import pos_to_string_converter
print("Finished importing " + __file__)

def check(text):
    __result=""
    __pos=nlp_funcs.pos_tokenize(text)
    __verb=[]

    if __pos[-1][0]=="?": #convert interrogative to imperative
            __verb=verb_finder.find_only_verb_question(text,__pos)
            print("The sentence is interrogative.")
            __pos[__verb[0]][0]=__pos[__verb[0]][3].title()
            __pos[-1][0]="."
            __pos[-1][2]="."
            phrase_after_token=[__pos[i] for i in list(range(__verb[0],len(__pos)))]
            __result=pos_to_string_converter.convert(phrase_after_token)
            print(__result)
            return __result
    else:
        __verb=verb_finder.find_only_verb(text,__pos)
        phrase_before_token=[__pos[i] for i in list(range(0,__verb[0]))]
        phrase_before=pos_to_string_converter.convert(phrase_before_token)        
        noun_phrases=nlp_funcs.find_noun_phrases(phrase_before)
        #convert imperative into passive
        if noun_phrases == [] and __pos[__verb[0]][3]==__pos[__verb[0]][0].lower():
                print("The sentence is imperative.")
                phrase_before_token[0][0]=phrase_before_token[0][0].lower()
                if phrase_before_token[-1][1]=="PUNCT":
                    phrase_before_token.pop()
                phrase_after_token=[__pos[i] for i in list(range(__verb[0],len(__pos)))]
                if phrase_after_token[-1][1]=="PUNCT":
                    for token in phrase_before_token:
                        phrase_after_token.insert(-1, token)
                __result="You are tasked to " + pos_to_string_converter.convert(phrase_after_token) 
                print(__result)
                return __result
        else:
            imp_pattern = [[{"POS":{"NOT_IN":["AUX"]}},{"POS":"AUX","OP":"?"},{"POS":"AUX","OP":"?"}, {"POS":"AUX"},{"TAG":"VBN"},{"LOWER":"to"},{"TAG": "VB"}]]
            matches=nlp_funcs.match(text, imp_pattern)
            if len(matches)>0:
                print("The sentence is in imperative passive form.")
            else: #convert declarative into imperative
                print("The sentence is declarative.")
                __pos[__verb[0]][0]=__pos[__verb[0]][3].title()
                phrase_after_token=[__pos[i] for i in list(range(__verb[0],len(__pos)))]
                __result=pos_to_string_converter.convert(phrase_after_token)
                print(__result)
                return __result
        
check("John has three apples.")