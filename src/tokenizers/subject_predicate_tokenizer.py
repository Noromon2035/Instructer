try:
    from converters import pos_to_string_converter
    from finders import verb_finder
except Exception as e:
    print(e)

verb_tags=("VERB","AUX")
def tokenize(text,pos):
    __subj=[]
    __pred=[]
    __final_vb_indexes=[]
    __result={}
    __pos=pos

    __final_vb_indexes=verb_finder.find(text, __pos)
    if __final_vb_indexes==[]:
        return
    
    for i in list(range(0,__final_vb_indexes[0])):
        __subj.append(__pos[i])

    for i in list(range(__final_vb_indexes[0],len(__pos))):
        __pred.append(__pos[i])

    __result["subject"]=pos_to_string_converter.convert(__subj)
    __result["predicate"]=pos_to_string_converter.convert(__pred)
    return __result
    