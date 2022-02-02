try:
    import re
    from nlps import nlp_matcher
    from finders import noun_phrase_finder
    from finders import verb_finder
    from converters import pos_to_string_converter
except Exception as e:
    print(e)
    
def check(nlp,text,pos):
    voice_mode={}
    text=re.search(r"\w.*",text).group()
    __pos=pos
    __verb=[]

    if is_interrogative(__pos): #convert interrogative to imperative
            print("The sentence is interrogative.")
            voice_mode["is_imperative"]=False

    else:
        __verb=verb_finder.find_only_verb(text,__pos)
        try:
            phrase_before_token=[__pos[i] for i in list(range(0,__verb[0]))]
        except:
            __verb.append(0)
            phrase_before_token=[__pos[i] for i in list(range(0,__verb[0]))]
        phrase_before=pos_to_string_converter.convert(phrase_before_token)        
        noun_phrases=noun_phrase_finder.find(nlp,phrase_before)

        #convert imperative into passive
        if (noun_phrases == [] or __pos[0][1]=="ADP") and __pos[__verb[0]][3]==__pos[__verb[0]][0].lower():
                print("The sentence is imperative.")
                voice_mode["is_imperative"]=True

        else:
            imp_pattern = [[{"POS":{"NOT_IN":["AUX"]}},{"POS":"AUX","OP":"?"},{"POS":"AUX","OP":"?"}, {"POS":"AUX"},{"TAG":"VBN"},{"LOWER":"to"},{"TAG": "VB"}]]
            matches=nlp_matcher.match(nlp,text, imp_pattern)

            if len(matches)>0:
                print("The sentence is in imperative passive form.")
                voice_mode["is_imperative"]=True

            else:
                print("The sentence is declarative.")
                voice_mode["is_imperative"]=False

    return voice_mode
    
def is_interrogative(pos):
    #Criteria: 5W1H or AUX pos
    question_words=("who","when","what","where","why","whose","how")
    if pos[-1][0]=="?":
        return True
    elif (pos[0][0].lower() in question_words or pos[0][1] == "AUX") and pos[0][0].lower() not in ("do","don't"):
        return True
    else:
        return False