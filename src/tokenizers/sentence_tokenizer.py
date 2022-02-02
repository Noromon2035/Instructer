#The backtick shows the start of the imperative sentence without the conjunction
#The ^ shows the location after the verb

try:
    from tokenizers import clause_tokenizer
    from converters import pos_to_string_converter
    from checkers import voice_checker
except Exception as e:
    print(e)

def handle_clauses(nlp,tokens):
    sentences=[]
    sentence=""

    for i in list(range(0,len(tokens["raw_clauses"]))):
        clause=tokens["clauses"][i]
        clause_str=tokens["raw_clauses"][i]
        voice=voice_checker.check(nlp,clause_str[1],clause[1])

        #getting the whole clause
        full_clause=[]
        full_clause_str=""
        punctuated=False

        #adding the conjuctions
        for pos in clause[0]:
            if sentence!="":
                full_clause.append(pos)
            elif pos[0].lower()!="and" and pos[1]!="PUNCT":
                full_clause.append(pos)
            if pos[1]=="PUNCT":
                punctuated=True
        
        #adding the clauses
        verb_found=False
        after_clause=[]
        for pos in clause[1]:
            after_clause.append(pos)
            if pos[1]=="VERB" and voice["is_imperative"]==True and verb_found==False:
                verb_found=True
                after_clause.append(['^', 'PUNCT', '^', '^'])
        if voice["is_imperative"]==True and verb_found==False:
            after_clause.insert(1,['^', 'PUNCT', '^', '^'])
        for pos in after_clause:
            full_clause.append(pos)

        #ends the sentence with .
        if voice["is_imperative"]==True and full_clause[-1][1]!="PUNCT":
            full_clause.append(['.', 'PUNCT', '.', '.'])

        #adding to sentence group
        full_clause_str=pos_to_string_converter.convert(full_clause)
        if voice["is_imperative"]==True:
            full_clause_str="`{}".format(full_clause_str)
        if sentence=="" or punctuated==True:
            sentence+=full_clause_str
        else:
            sentence+=" "+ full_clause_str


        if voice["is_imperative"]==True:
            if sentence[0]=="`":
                sentence= "`" + sentence[1].upper() + sentence[2:]
            else:
                sentence=sentence[0].upper()+sentence[1:]
            sentences.append(sentence)
            sentence=""
    if sentence !="":
        sentences.append(sentence)
    print(sentences)
    return sentences



def convert(nlp,text,pos):

    __tokens={}
    __raw_clauses=[]

    __tokens["clauses"]=clause_tokenizer.tokenize(text, pos)

    for clause in __tokens["clauses"]:
        temp_clause=[]
        for token in clause:
            text_token=pos_to_string_converter.convert(token)
            temp_clause.append(text_token)
        __raw_clauses.append(temp_clause)
    

    print("\nSentence structures were found.")
    __tokens["raw_clauses"]=__raw_clauses
    print(__tokens["raw_clauses"])

    sentences=handle_clauses(nlp,__tokens)
    return sentences

if __name__ =="__main__":
    from tokenizers import pos_tokenizer
    import spacy
    nlp = spacy.load("en_core_web_sm")

    text2="Once it can be safely assumed that the base of the flour-based cake has reached a satisfactory level of cook, firmly grasp handle of your flipping leverage tool with flip-side up and thrust forward using shoulder, engaging glenohumeral joint for smooth motion"
    pos=pos_tokenizer.pos_tokenize(text2)
    convert(nlp,text2,pos)
