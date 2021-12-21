print("Importing " + __file__)
import pos_to_string_converter
import verb_finder
print("Finished importing " + __file__)

verb_tags=("VERB","AUX")
def tokenize(text,pos):
    __subj=[]
    __pred=[]
    __final_vb_indexes=[]
    __result={}
    __pos=pos

    __final_vb_indexes=verb_finder.find(text, __pos)
    
    for i in list(range(0,__final_vb_indexes[0])):
        __subj.append(__pos[i])

    for i in list(range(__final_vb_indexes[0],len(__pos))):
        __pred.append(__pos[i])

    __result["subject"]=pos_to_string_converter.convert(__subj)
    __result["predicate"]=pos_to_string_converter.convert(__pred)
    print(__result)
    return __result