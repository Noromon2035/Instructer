try:
    import re
    from finders import synsets_finder
except Exception as e:
    print(e)
    
verb_tags=("VERB","AUX")
before_verb_tags=("VERB","AUX","PART")
modals=("can","could","should","shall","would","will","must","may","might")

def find(text,pos):
    __pos=pos
    __vb_indexes=[]
    __final_vb_indexes=[]

    for i in list(range(0,len(__pos))):
        if __pos[i][1] in verb_tags:
            __vb_indexes.append(i)
    
    if __vb_indexes==[]:
        __pos=verb_finder_backup(__pos)
        for i in list(range(0,len(__pos))):
            if __pos[i][1] == "VERB":
               __vb_indexes.append(i)
            
    for i in list(range(0,len(__vb_indexes))):
        temp_index=__vb_indexes[i]
        if __pos[temp_index][2]=="VBG":
            has_aux=True
            counter=0
            while has_aux == True:
                try:
                    if __pos[temp_index-counter][1] in before_verb_tags and __pos[temp_index-counter][0]!="'s":
                        if temp_index-counter not in __final_vb_indexes:
                            __final_vb_indexes.append(temp_index-counter)
                        has_aux=True
                    else:
                        has_aux=False
                except:
                    has_aux=False
                counter+=1
        else:
            if __vb_indexes[i] not in __final_vb_indexes:
                __final_vb_indexes.append(__vb_indexes[i])
    __final_vb_indexes.sort()
    return __final_vb_indexes

def find_only_verb(text,pos):
    __pos=pos
    __vb_indexes=[]
    __final_vb_indexes=[]

    for i in list(range(0,len(__pos))):
        if __pos[i][0] not in modals and (__pos[i][1] == "VERB" or __pos[i][1] == "AUX" or re.findall("n't$",__pos[i][0])):
            __vb_indexes.append(i)
    
    if __vb_indexes==[]:
        __pos=verb_finder_backup(__pos)
        for i in list(range(0,len(__pos))):
            if __pos[i][1] == "VERB":
               __vb_indexes.append(i)

    for i in list(range(0,len(__vb_indexes))):
        temp_index=__vb_indexes[i]
        if __pos[temp_index][2]=="VBG":
            try:
                if __pos[temp_index-1][1]=="AUX":
                    __final_vb_indexes.append(__vb_indexes[i])
            except:
                continue
        else:
            __final_vb_indexes.append(__vb_indexes[i])

    
    return __final_vb_indexes

def find_only_verb_question(text,pos):
    __pos=pos
    __vb_indexes=[]
    __final_vb_indexes=[]

    for i in list(range(0,len(__pos))):
        if __pos[i][1] == "VERB":
            __vb_indexes.append(i)
    
    if __vb_indexes==[]:
        __pos=verb_finder_backup(__pos)
        for i in list(range(0,len(__pos))):
            if __pos[i][1] == "VERB":
               __vb_indexes.append(i)

    for i in list(range(0,len(__vb_indexes))):
        temp_index=__vb_indexes[i]
        __final_vb_indexes.append(__vb_indexes[i])

    
    print(__final_vb_indexes)
    return __final_vb_indexes

def verb_finder_backup(pos):
    __prep_indexes=[]
    count=0
    for token in pos:
        if token[1]=="ADP":
            __prep_indexes.append(count)
        count+=1

    __probable_verb_index=0
    highest_verb_ratio=0
    for index in __prep_indexes:
        try:
            noun_count=synsets_finder.find_noun_synsets_count(pos[index-1][0])
            verb_count=synsets_finder.find_verb_synsets_count(pos[index-1][0])
            verb_ratio=(verb_count+1)/(noun_count+1)
            if verb_ratio>highest_verb_ratio:
                highest_verb_ratio=verb_ratio
                __probable_verb_index=index-1
        except:
            continue
    try:
        pos[__probable_verb_index][1]="VERB"
        pos[__probable_verb_index][2]="VB"
    except:
        pos=[]
    return pos
    
