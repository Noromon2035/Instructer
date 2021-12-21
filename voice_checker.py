print("Importing " + __file__)
import nlp_funcs
import verb_finder
import pos_to_string_converter
print("Finished importing " + __file__)

def check(text):
    __result=""
    __pos=nlp_funcs.pos_tokenize(text)

    __verb=verb_finder.find_only_verb(text,__pos)
    if __pos[__verb[0]][1]=="VERB":
        phrase_before_token=[__pos[i] for i in list(range(0,__verb[0]))]
        phrase_before=pos_to_string_converter.convert(phrase_before_token)        
        noun_phrases=nlp_funcs.find_noun_phrases(phrase_before)
        if noun_phrases == []:
            __lemmas=nlp_funcs.lemmatize(text)
            if __lemmas[__verb[0]]==__pos[__verb[0]][0].lower():
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

check("First, dive in the water with your son.")