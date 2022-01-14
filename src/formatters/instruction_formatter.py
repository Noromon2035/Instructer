
def format(sentence_list):
    enumerated=[]
    if len(sentence_list)==1:
        sentence_token={}
        sentence=sentence_list[0][0]
        sentence_token["text"]=sentence
        sentence_token["questions"]=sentence_list[0][1]
        sentence_token["predicate"]=sentence_list[0][2]
        enumerated.append(sentence_token)
    else:
        for i in list(range(0,len(sentence_list))):
            sentence_token={}
            sentence="{}. {}\n".format(i+1,sentence_list[i][0])
            sentence_token["text"]=sentence
            sentence_token["questions"]=sentence_list[i][1]
            sentence_token["predicate"]=sentence_list[i][2]
            enumerated.append(sentence_token)
    return enumerated