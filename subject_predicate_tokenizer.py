print("Importing " + __file__)
import pos_tokenizer
import pos_to_string_converter
print("Finished importing " + __file__)

verb_tags=("VERB","AUX")
def tokenize(text):
    __subj=[]
    __pred=[]
    __vb_indexes=[]
    __final_vb_indexes=[]
    __pos=pos_tokenizer.tokenize(text)

    for i in list(range(0,len(__pos))):
        if __pos[i][1] in verb_tags:
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
    
    for i in list(range(0,__final_vb_indexes[0])):
        __subj.append(__pos[i])

    if __pos[__final_vb_indexes[-1]][2] == "VBG":
        for i in list(range(__final_vb_indexes[-2],len(__pos))):
            __pred.append(__pos[i])
    else:
        for i in list(range(__final_vb_indexes[-1],len(__pos))):
            __pred.append(__pos[i])

    print(pos_to_string_converter.convert(__subj))
    print(pos_to_string_converter.convert(__pred))
    print(__vb_indexes, __final_vb_indexes)

tokenize("The eating boy is eating foods.")