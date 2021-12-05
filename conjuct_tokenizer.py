print("Importing " + __file__)
import spacy
import re
print("Finished importing " + __file__)

nlp = spacy.load("en_core_web_sm")

def conj_clause_processor(conj_index, pos):
    #Then check if it's seperating independent clauses
    current=1
    previous=0
    current_cindex=0
    __passed_conj_index=[]
    __passed_conj_clause=[]
    while current < len(conj_index)+1:
        try:
            current_cindex=conj_index[current]
        except:
            current_cindex=len(pos)

        temp_clause=[]
        for i in list(range(conj_index[previous],current_cindex)):
            temp_clause.append(pos[i])

        #Start checking if it's seperating clauses
        if pos[conj_index[previous]][0]=="and" or pos[conj_index[previous]][0]=="or":
            for clause in temp_clause:
                if clause[1]=="AUX" or clause[1]=="VERB":
                    __passed_conj_index.append(conj_index[previous])
                    __passed_conj_clause.append(temp_clause)
                    break
        else:
            __passed_conj_index.append(conj_index[previous])
            __passed_conj_clause.append(temp_clause)
        previous=current
        current+=1

    return {"index":__passed_conj_index, "clause":__passed_conj_clause}

def tokenize(text):
    __pos=[]
    __conjuctions={}
    __conj_index=[]

    __doc = nlp(text)

    for token in __doc:
        __pos.append([token.text, token.pos_, token.tag_])

    #First find all conjuctions
    for i in list(range(0, len(__pos))):
        if __pos[i][1]=="CCONJ" or __pos[i][1]=="SCONJ":
            __conj_index.append(i)
    
    __conjuctions=conj_clause_processor(__conj_index, __pos)
    __conjuctions=conj_clause_processor(__conjuctions["index"], __pos)
    #Note. Both keys and values have the same size. To access both, just use one of their indexes.
    return __conjuctions