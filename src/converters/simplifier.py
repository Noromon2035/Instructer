try:
    import pyinflect
    import statistics
    import json
    from gensim.models import KeyedVectors
    from nltk.corpus import wordnet as wn
    from nltk.corpus import stopwords
    from tokenizers import pos_tokenizer
    from converters import pos_to_string_converter
except Exception as e:
    print(e)

sw = stopwords.words('english')
wordnet_pos=("NOUN","VERB","ADV","ADJ")
wordvec = KeyedVectors.load("instruct_vector.wordvectors", mmap='r')
with open("occurences.json", "r") as fp:
    occurences_json=json.load(fp)
occur_quantile=11

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

    orig_token_similarities=[]
    for context in context_tokens:
        try:
            orig_token_similarities.append(wordvec.similarity(orig_token[3],context[3]))
        except:
            orig_token_similarities.append(0)

    total_errors=[]
    for token in above_median:
        total_error=[]
        total_error.append(token[0])
        error=0
        for i in list(range(0,len(orig_token_similarities))):
            try:
                similarity=wordvec.similarity(token[0],context_tokens[i][3])
                error+=abs(similarity-orig_token_similarities[i])
            except:
                error+=0
        total_error.append(error)
        total_errors.append(total_error)
    
    best_synonym=total_errors[0][0]
    lowest_error=total_errors[0][1]
    for token in total_errors:
        if token[1]<lowest_error:
            best_synonym=token[0]
            lowest_error=token[1]
    return best_synonym

def best_synonym_2(orig_token,tokens,pos):
    if len(tokens)<=0:
        return orig_token[3]
    data_set=[token[1] for token in tokens]
    median=statistics.median(data_set)
    for token in tokens:
        if token[0]==orig_token[3]:
            if token[1]<median:
                above_median=[token for token in tokens if token[1]>median]
                return best_synonym_1(orig_token,above_median,pos)
            else:
                return token[0]

def find_occurences(word):
    count=0
    try:
        count=occurences_json[word]
    except:
        count=0
    return count

def simplify(nlp,pos):
    pos_without_sw = [token for token in pos if token[0].lower() not in sw and token[1] in wordnet_pos]
    indexes_without_sw = [i for i in list(range(0,len(pos))) if pos[i][0].lower() not in sw and pos[i][1] in wordnet_pos]

    for i in list(range(0,len(pos_without_sw))):
        pos_without_sw[i].append(i)
        pos_without_sw[i].append(indexes_without_sw[i])
    del indexes_without_sw

    final_synonyms=[]
    for token in pos_without_sw:
        tag=spacy_pos_to_wordnet(token[1])
        synonyms=wn.synsets(token[3].lower(), pos=tag)

        if find_occurences(token[3])>occur_quantile:
            final_synonyms.append(token[3])
        else:
            #get all synonyms of each token as raw_string
            print(token[3])
            raw_synonyms=set()
            raw_synonyms.add(token[3])
            for syn in synonyms:
                raw_syns=syn.lemmas()
                for raw_syn in raw_syns:
                    raw=str(raw_syn.name())
                    raw_synonyms.add(raw.replace("_"," "))  
                    
            
            #find occurences of each tokens
            synonym_tokens=[]
            for syn in raw_synonyms:
                occurences=find_occurences(syn)
                print(syn+":"+str(occurences))
                if occurences!=0:
                    synonym_tokens.append([syn,occurences])
            
            #choose the best synonym
            final_synonym=best_synonym_2(token,synonym_tokens,pos_without_sw)
            final_synonyms.append(final_synonym)
        print("Best synonym: {}\n".format(final_synonyms[-1]))

    changed_pos=[] #[index,tag]
    for i in list(range(0,len(final_synonyms))):
        #if lemma of orig not equal synonym
        if pos_without_sw[i][3]!=final_synonyms[i]:
            pos_without_sw[i][0],pos_without_sw[i][3]=final_synonyms[i],final_synonyms[i]
            changed_pos.append([pos_without_sw[i][5],pos_without_sw[i][2]])

    new_text=pos_to_string_converter.convert(pos)
    doc_tokens=pos_tokenizer.tokenize(nlp,new_text)
    for token in changed_pos:
        morphed=""
        if pos[token[0]][0]!=pos[token[0]][3]:
            morphed=doc_tokens[token[0]]._.inflect(token[1])
        if morphed !=None and morphed!="":
            pos[token[0]][0]=morphed
    return pos_to_string_converter.convert(pos)