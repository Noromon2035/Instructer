
verb_tags=("VERB","AUX")

def find(text,pos):
    __vb_indexes=[]
    __final_vb_indexes=[]

    for i in list(range(0,len(pos))):
        if pos[i][1] in verb_tags:
            __vb_indexes.append(i)
            
    for i in list(range(0,len(__vb_indexes))):
        temp_index=__vb_indexes[i]
        if pos[temp_index][2]=="VBG":
            try:
                if pos[temp_index-1][1]=="AUX":
                    __final_vb_indexes.append(__vb_indexes[i])
            except:
                continue
        else:
            __final_vb_indexes.append(__vb_indexes[i])

    print(__final_vb_indexes)
    return __final_vb_indexes
